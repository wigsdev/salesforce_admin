# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- **UI/UX**: Dynamic Project Dashboard (`/lumina/dashboard`).
  - Added capability to create/delete custom days.
  - Added capability to add/edit/delete tasks dynamically.
  - Added "Sticky Footer" layout support for short content pages.
  - Added "Add Task" manual input field for rapid entry.
- **Frontend**: Clean and Minimalist Mobile Brand Icon (Cloud SVG).
- **Quality**: Implemented extensive CI/CD Pipeline.
  - **GitHub Actions**: Automated testing workflow on push/PR (`.github/workflows/ci.yml`).
  - **Pre-commit Hooks**: Automatic local verification before commit (`scripts/run_tests.bat`).
  - **Code Standard**: Enforced Black (formatting) and Ruff (linting) standards.
  - **Testing**: Added Pytest suite for Unit (Security) and E2E (Auth) tests.
- **Deployment**: Added Render Blueprint (`render.yaml`) and build scripts (`scripts/build.sh`) for automated production deployment.

### Changed
- **UI/UX**: Refactored Lumina Dashboard to match specific Curriculum Tasks (Classes 7-10).
- **UI/UX**: Removed distracting metrics from Dashboard (Sprint Title, Global Progress).
- **Styles**: Migrated legacy CSS to Tailwind Layers for better build performance.
- **Layout**: Fixed padding issues (32px) and select arrow alignment in Dashboard.

### Fixed
- **Bug**: Fixed `input.css` build pipeline to correctly include custom styles.
- **Bug**: Fixed mobile menu icon visibility issues.
