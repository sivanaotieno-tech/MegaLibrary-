# MegaLibrary

MegaLibrary is a Mihon-compatible beta distribution for four manga source entries:

- MangaDex
- VIZ Manga
- VIZ Shonen Jump
- Read Jujutsu Kaisen Manga Online

## Build status

The GitHub Actions workflow builds three Android extension APKs from pinned upstream Keiyoushi source modules. The VIZ APK exposes two source entries, so the bundle contains all four requested catalogues.

**Important:** this first installable beta is a branded source bundle, not yet a single unified search catalogue. Mihon will show the sources separately. Unified cross-source search and safe bulk-library management are later development work and are not claimed as implemented.

## Install

1. Open this repository's **Actions** tab.
2. Open the latest successful **Build MegaLibrary Mihon extensions** run.
3. Download the `MegaLibrary-Mihon-APKs` artifact.
4. Extract the ZIP on Android.
5. Open each APK and allow installation when Android prompts.
6. Open Mihon and check Browse → Extensions / Sources.

The APKs use debug signing for this beta build. They are for testing, not a production release/update channel. The build artifact is not yet a Mihon extension-repository index.

## Source and access rules

- VIZ login, subscription, locked-chapter and country restrictions remain in force.
- MangaDex content ratings and API restrictions remain in force.
- No DRM, paywall, login, or regional restriction is bypassed.
- Catalogue availability depends on each provider and its source implementation.

## Development

The workflow fetches the Keiyoushi extension source repository at a pinned commit, applies MegaLibrary package/display-name changes, then builds the three APKs with Gradle.

See [the implementation plan](docs/IMPLEMENTATION_PLAN.md) and [third-party notices](THIRD_PARTY_NOTICES.md).
