# Implementation plan

## Beta 1: installable source bundle

- Build MangaDex as a MegaLibrary-branded Mihon extension.
- Build VIZ as one extension exposing VIZ Manga and VIZ Shonen Jump.
- Build Read Jujutsu Kaisen Manga Online as a MegaLibrary-branded Mihon extension.
- Keep upstream provider behaviour and access checks intact.
- Build debug-signed APKs in GitHub Actions for device testing.

## What Beta 1 does not do

- It does not merge the four catalogues into one unified search result list.
- It does not issue bulk-add commands to Mihon's private library database.
- It does not bypass provider login, subscription, DRM, country, or content-rating restrictions.
- It does not publish a Mihon repository index or a production signing key.

## Next milestones

1. Verify that the APKs build successfully in GitHub Actions.
2. Test installation and source behaviour on Mihon 0.21.3 / Android 14.
3. Add an optional unified catalogue adapter, subject to provider APIs and terms.
4. Investigate a supported Mihon-native bulk-add workflow; do not write to private app databases.
5. Set up a stable signing key and publish a compatible Mihon extension repository only after signing and index generation are verified.
