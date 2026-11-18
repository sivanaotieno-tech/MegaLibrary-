# MegaLibrary

MegaLibrary is a planned Mihon extension for discovering manga across four user-selected catalogues:

- MangaDex
- VIZ Manga
- VIZ Shonen Jump
- Read Jujutsu Kaisen Manga Online

The target is **Mihon 0.21.3+ on Android**.

## Installation goal

The intended distribution is a Mihon-compatible extension repository, so MegaLibrary can be installed from Mihon's Extensions screen rather than requiring users to build the project.

A repository URL and installable APK will be published only after the extension has been built, signed, and tested. This repository is not yet an installable extension store.

## Important source limitations

- VIZ login, subscription, chapter-lock, and regional-availability rules must be respected.
- MangaDex content ratings and API policies must be respected.
- Source catalogues may paginate, rate-limit, require authentication, or restrict availability. "All titles" means all entries the supported catalogue endpoints make available under their rules; it cannot override those restrictions.
- MegaLibrary does not host manga or bypass paywalls, DRM, or access controls.

## Development status

This repository is the project home. The implementation, build pipeline, signed APK, and Mihon repository index must be completed and verified before installation instructions are published.

## Target platform

- Mihon 0.21.3
- Android 14 / SDK 34
- Kotlin extension using the compatible Mihon/Keiyoushi extension API

## License

To be decided before the first public release.