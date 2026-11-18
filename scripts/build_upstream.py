#!/usr/bin/env python3
"""Build MegaLibrary-branded Mihon APKs from pinned Keiyoushi source modules."""

from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = ROOT / ".upstream"
OUTPUT = ROOT / "output"
UPSTREAM_URL = "https://github.com/keiyoushi/extensions-source.git"
UPSTREAM_COMMIT = "f1d882a93ef34a33dc4f4467753ad5f99eab43f4"

MODULES = [
    ":src:all:mangadex",
    ":src:en:vizshonenjump",
    ":src:en:readjujutsukaisenmangaonline",
]


def run(*args: str, cwd: Path | None = None) -> None:
    print("+", " ".join(args), flush=True)
    subprocess.run(args, cwd=cwd, check=True)


def replace_once(path: Path, old: str, new: str) -> None:
    content = path.read_text(encoding="utf-8")
    if old not in content:
        raise RuntimeError(f"Expected text not found in {path}: {old!r}")
    path.write_text(content.replace(old, new, 1), encoding="utf-8")


def patch_module(path: Path, replacements: list[tuple[str, str]]) -> None:
    content = path.read_text(encoding="utf-8")
    for old, new in replacements:
        if old not in content:
            raise RuntimeError(f"Expected text not found in {path}: {old!r}")
        content = content.replace(old, new, 1)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    if UPSTREAM.exists():
        shutil.rmtree(UPSTREAM)
    run("git", "clone", "--filter=blob:none", UPSTREAM_URL, str(UPSTREAM))
    run("git", "checkout", UPSTREAM_COMMIT, cwd=UPSTREAM)

    patch_module(
        UPSTREAM / "src/all/mangadex/build.gradle.kts",
        [
            ('name = "MangaDex"', 'name = "MegaLibrary MangaDex"'),
            ('versionCode = 4', 'pkgName = "all.megalibrarymangadex"\n    versionCode = 5'),
        ],
    )
    patch_module(
        UPSTREAM / "src/en/vizshonenjump/build.gradle.kts",
        [
            ('name = "VIZ"', 'name = "MegaLibrary VIZ"'),
            ('versionCode = 31', 'pkgName = "en.megalibraryviz"\n    versionCode = 32'),
            ('name = "VIZ Shonen Jump"', 'name = "MegaLibrary - VIZ Shonen Jump"'),
            ('name = "VIZ Manga"', 'name = "MegaLibrary - VIZ Manga"'),
        ],
    )
    patch_module(
        UPSTREAM / "src/en/readjujutsukaisenmangaonline/build.gradle.kts",
        [
            ('name = "Read Jujutsu Kaisen Manga Online"', 'name = "MegaLibrary JJK"'),
            ('versionCode = 0', 'pkgName = "en.megalibraryjjk"\n    versionCode = 1'),
        ],
    )

    gradle = UPSTREAM / "gradlew"
    gradle.chmod(gradle.stat().st_mode | 0o111)
    tasks = [f"{module}:assembleDebug" for module in MODULES]
    run(str(gradle), *tasks, cwd=UPSTREAM)

    OUTPUT.mkdir(exist_ok=True)
    for module in MODULES:
        module_path = UPSTREAM / module.removeprefix(":").replace(":", "/")
        apk_dir = module_path / "build/outputs/apk/debug"
        apks = list(apk_dir.glob("*.apk"))
        if not apks:
            raise RuntimeError(f"No APK generated for {module} in {apk_dir}")
        for apk in apks:
            target = OUTPUT / apk.name
            shutil.copy2(apk, target)
            print(f"Collected {target}")

    shutil.copy2(UPSTREAM / "LICENSE", OUTPUT / "LICENSE")
    (OUTPUT / "THIRD_PARTY_NOTICES.txt").write_text(
        "MegaLibrary beta APKs are built from the following upstream Mihon extension sources:\n"
        "- MangaDex extension from keiyoushi/extensions-source\n"
        "- VIZ extension from keiyoushi/extensions-source\n"
        "- Read Jujutsu Kaisen Manga Online extension from keiyoushi/extensions-source\n\n"
        "The upstream project is licensed under Apache License 2.0. The build applies only "
        "MegaLibrary package/display-name changes; provider behaviour remains subject to "
        "the upstream source implementations and each provider's own terms, authentication, "
        "subscription and regional restrictions.\n\n"
        "Upstream: https://github.com/keiyoushi/extensions-source\n"
        f"Pinned commit: {UPSTREAM_COMMIT}\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
