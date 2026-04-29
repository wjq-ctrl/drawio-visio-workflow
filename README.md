# drawio-visio-workflow

A Codex skill for inspecting `.drawio` diagrams, extracting their structure, and rebuilding them as editable Microsoft Visio `.vsdx` files.

## What this skill does

This skill is meant for workflows where:

- the source diagram is a `draw.io` / `.drawio` file
- the output needs to be an editable Visio file
- the diagram may also need visual restyling before conversion

Typical uses:

- convert a draw.io flowchart into Visio
- restyle a technical diagram for an academic thesis
- inspect draw.io XML before manual or scripted Visio reconstruction
- automate repeated drawio-to-visio conversion work

## Repository structure

```text
drawio-visio-workflow/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ workflow.md
│  └─ style-guidelines.md
└─ scripts/
   ├─ extract_drawio_cells.py
   └─ visio_helpers.ps1
```

## Requirements

- Windows
- Microsoft Visio installed locally
- PowerShell
- Python 3

## Included resources

### `SKILL.md`

Defines when the skill should trigger and how Codex should use it.

### `references/workflow.md`

Describes the end-to-end workflow:

1. inspect the source `.drawio`
2. extract diagram cells
3. choose the reconstruction style
4. generate a Visio reconstruction script
5. create and verify the `.vsdx`

### `references/style-guidelines.md`

Provides styling guidance for:

- academic paper figures
- optimized presentation diagrams
- original-layout preservation

### `scripts/extract_drawio_cells.py`

Parses a `.drawio` file and emits a JSON summary of:

- vertices
- edges
- labels
- geometry
- style strings

Example:

```bash
python scripts/extract_drawio_cells.py path/to/file.drawio
```

### `scripts/visio_helpers.ps1`

Provides reusable PowerShell helper functions for Visio COM drawing, including:

- rectangles
- text boxes
- arrows
- coordinate conversion helpers

Use these helpers when building a per-diagram Visio reconstruction script.

## How to use this as a Codex skill

Place this folder where Codex can discover skills, or reference it explicitly by path.

Typical prompt:

```text
Use $drawio-visio-workflow to inspect a .drawio file, extract its structure, restyle it for an academic paper, and rebuild it as an editable .vsdx.
```

## Notes

- This skill treats the `.drawio` file as the structural source of truth.
- For thesis figures, the recommended default style is the academic style in `references/style-guidelines.md`.
- If Windows PowerShell shows garbled Chinese text, rewrite scripts as UTF-8 BOM before execution.
