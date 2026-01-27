# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Project Overview

GoodNotes Template Generator - a Python utility that programmatically generates PDF templates and sample notes designed for GoodNotes (iOS/iPad note-taking app). Documentation and content are written in **Korean**.

The project has two core functions:
1. **Template generation** (`create_templates.py`) - Produces 11 blank PDF templates (lined, dotted, grid, Cornell, music sheet, weekly planner, etc.)
2. **Sample note generation** (`create_sample_notes.py`) - Produces 5 realistic example notes with filled-in content (study notes, meeting minutes, journal, recipe, book notes)

## Repository Structure

```
/
├── create_templates.py      # Generates 11 blank PDF templates
├── create_sample_notes.py   # Generates 5 sample notes with content
├── templates/               # Output directory for blank templates (11 PDFs)
├── samples/                 # Output directory for sample notes (5 PDFs)
├── README.md                # Project documentation (Korean)
├── .gitignore               # Standard Python gitignore
└── CLAUDE.md                # This file
```

## Key Files

### `create_templates.py` (229 lines)
Generates 11 blank PDF templates using ReportLab. Each template type has its own function:

| Function | Output | Description |
|---|---|---|
| `create_lined_template()` | 01, 02, 10, 11 | Lined notebook (reused with different spacing/colors) |
| `create_dotted_template()` | 03 | Dotted grid notebook |
| `create_grid_template()` | 04, 05 | Grid/graph paper (reused with different spacing) |
| `create_blank_template()` | 06 | Blank page |
| `create_cornell_template()` | 07 | Cornell notes layout (cue column + summary area) |
| `create_music_template()` | 08 | Music staff paper |
| `create_weekly_planner()` | 09 | Weekly planner with day sections |

**Module-level constants**: `OUTPUT_DIR`, `WIDTH`, `HEIGHT`, `LIGHT_GRAY`, `MEDIUM_GRAY`, `LIGHT_BLUE`, `LIGHT_PINK`

### `create_sample_notes.py` (597 lines)
Generates 5 example notes with real Korean-language content:

| Function | Output |
|---|---|
| `create_study_notes_python()` | Python study notes with code examples |
| `create_meeting_notes()` | Project meeting minutes with action items |
| `create_daily_journal()` | Personal daily journal entry |
| `create_recipe_note()` | Tomato cream pasta recipe |
| `create_book_notes()` | Book notes in Cornell note style |

## Technology Stack

- **Language**: Python 3
- **PDF library**: ReportLab (`reportlab`)
  - `reportlab.lib.pagesizes` (A4)
  - `reportlab.pdfgen.canvas` (Canvas-based PDF drawing)
  - `reportlab.lib.units` (mm for measurements)
  - `reportlab.lib.colors` (Color definitions)
  - `reportlab.pdfbase` / `reportlab.pdfbase.ttfonts` (font handling, imported in sample notes)
- **Optional**: Pillow (mentioned in README for image handling, not currently used)

## Commands

### Setup
```bash
pip install reportlab Pillow
```

### Generate Templates
```bash
python3 create_templates.py     # Outputs 11 PDFs to templates/
python3 create_sample_notes.py  # Outputs 5 PDFs to samples/
```

There is no build system, test framework, linter, or CI/CD pipeline. Scripts are run directly.

## Code Conventions

### Architecture Patterns
- **One function per template type** - each function creates a complete PDF independently
- **`main()` function orchestrates** - calls all generator functions and prints summary
- **Auto-creates output directories** - `os.makedirs(OUTPUT_DIR, exist_ok=True)` at module level
- **Console output** - each function prints `✓ Created: {filename}` on success

### Naming Conventions
- **Functions**: `create_<type>_template()` or `create_<type>_notes()` - verb-based, descriptive
- **Constants**: UPPER_SNAKE_CASE at module level (`OUTPUT_DIR`, `WIDTH`, `HEIGHT`, color definitions)
- **Variables**: lowercase with underscores (`line_spacing`, `dot_size`, `cue_column_width`)
- **Output files**: numbered prefix for templates (`01_`, `02_`, ...), `example_` prefix for samples

### Style
- 4-space indentation
- Korean docstrings on all functions
- Korean for user-facing strings and comments; English for code identifiers
- Minimal comments - code is self-explanatory
- No type hints
- Standard Python shebang: `#!/usr/bin/env python3`

### PDF Drawing Conventions
- **Page size**: A4 (210 x 297mm) via `reportlab.lib.pagesizes.A4`
- **Margins**: 20mm standard (`20*mm`), 15mm for weekly planner
- **Measurements**: All in millimeters using ReportLab's `mm` unit
- **Colors**: Defined as `Color(r, g, b, alpha=...)` constants at module level
- **Fonts**: Helvetica family only (Helvetica, Helvetica-Bold, Helvetica-Oblique) - built into ReportLab, no external font files needed
- **Drawing pattern**: Create canvas -> set styles -> draw elements -> `c.save()`

### Adding New Templates
Follow the existing pattern:
1. Define a new function `create_<name>_template(filename, ...)` or `create_<name>_notes()`
2. Create a `canvas.Canvas(filename, pagesize=A4)`
3. Draw background elements first, then foreground content
4. Call `c.save()` and print confirmation
5. Add the call to `main()` with the output path

## Important Notes

- Generated PDFs are committed to the repository (not gitignored)
- The `templates/` and `samples/` directories contain output artifacts, not source files
- Korean text renders correctly only with fonts that support Korean characters; Helvetica is used as a fallback (some Korean glyphs may not render in all PDF viewers)
- No dependency lock file exists - install `reportlab` and optionally `Pillow` manually
- License: free to use, modify, and distribute (stated in README)
