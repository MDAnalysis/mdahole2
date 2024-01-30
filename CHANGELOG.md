# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
The rules for this file:
  * entries are sorted newest-first.
  * summarize sets of changes - don't reproduce every git log comment here.
  * don't ever delete anything.
  * keep the format consistent:
    * do not use tabs but use spaces for formatting
    * 79 char width
    * YYYY-MM-DD date format (following ISO 8601)
  * accompany each entry with github issue/PR number (Issue #xyz)
-->

## [0.4.0] -- 2024-01-30

### Authors
<!-- GitHub usernames of contributors to this release -->
- ianmkenney
- IAlibay
- lilyminium

### Added
- Support for Python 3.12 (PR #42)
- mdahole2 confirmed to work on macOS and is now included in CI (PR #35)
- Added and updated documentation (PR #48, Issue #33)
<!-- New added features -->

### Fixed
- Duecredit paths now point to mdahole2
- Updated to modern matplotlib ``get_cmap`` (PR #39)
<!-- Bug fixes -->

### Changed
- Version handling is now handled via versioningit (PR #41)
- Switched to ``shutil.which`` instead of custom function (PR #41)

### Deprecated
<!-- Soon-to-be removed features -->

### Removed
<!-- Removed features -->

## [0.3.0] -- 2023-07-12

### Authors
- ianmkenney

### Changed
- bumped Python support from 3.8+ to 3.9+
- test environment file now points to the conda-forge hole2 binary (#15)
- package name shortened from mdakithole2 to mdahole2 (#21)

## [0.2.0] -- 2023-05-04

The original `MDAnalysis.analysis.hole2` was written by Lily Wang in 2020 and
had been part of MDAnalysis since release 1.0.0,
https://docs.mdanalysis.org/2.6.1/documentation_pages/analysis/hole2.html.
Ian Kenney created the `mdakithole2` MDAKit in 2022, based on the original code
in MDAnalysis. Additional contributors to the original source code are listed
in the AUTHORS.md file.

### Authors
- ianmkenney
- IAlibay

### Added
- the core functionality of hole2-mdakit (and its tests) was implemented
  using the source code from MDAnalysis.analysis.hole2 (PR #1)
- GitHub actions CI workflow (PR #2 #3 #7)
- added historical authors from original source to AUTHORS.md (PR #4)
- documentation deployed to github pages (PR #11)

## Changed

[Unreleased]: https://github.com/MDAnalysis/mdahole2/compare/0.3.0...HEAD
[0.3.0]: https://github.com/MDAnalysis/mdahole2/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/MDAnalysis/mdahole2/releases/tag/0.2.0
