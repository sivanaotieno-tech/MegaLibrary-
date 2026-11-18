# MegaLibrary implementation plan

## Product target

One installable Mihon extension that provides a unified catalogue across the four confirmed source families:

1. MangaDex
2. VIZ Manga
3. VIZ Shonen Jump
4. Read Jujutsu Kaisen Manga Online

## Required behaviour

- Search and paginate each supported catalogue within its documented/public access rules.
- Normalize title metadata and deduplicate overlapping titles without losing source-specific identifiers.
- Preserve the originating source for chapter listing and reading.
- Respect VIZ authentication, subscription, regional and locked-chapter checks.
- Respect MangaDex content ratings, API limits and attributions.
- Handle unavailable sources independently so one provider outage does not break the others.

## Mihon integration constraints

A source extension cannot directly write to Mihon's private library database or command unrelated installed extensions. Library actions must use Mihon's supported source UI. No unsupported bulk-import API will be assumed.

## Release requirements

- Build against the compatible extension API.
- Verify the APK package ID, signature and metadata.
- Test installation and source discovery on Mihon 0.21.3 / Android 14.
- Publish the APK and a compatible repository index.
- Test adding the repository and installing/updating through Mihon's Extensions screen.

## Definition of done

The project is not considered released until the signed APK installs in Mihon, all four source adapters have been tested, catalogue pagination works, and provider restrictions are enforced.