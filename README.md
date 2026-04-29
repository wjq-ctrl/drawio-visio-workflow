# drawio-visio-workflow

A Codex skill for turning a rough diagram description, image description, or existing `.drawio` file into both editable `.drawio` and Microsoft Visio `.vsdx` outputs.

## What this skill does

This skill is meant for workflows where:

- the source is a rough process or framework description
- or the source is an image description
- or the source is an existing `draw.io` / `.drawio` file
- the output needs to include both editable `.drawio` and editable `.vsdx`
- the diagram may also need visual restyling before conversion

Typical uses:

- create a fresh flowchart from a text description
- optimize a rough diagram prompt before drawing
- retrieve similar reference diagrams before layout
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
│  ├─ input-refinement.md
│  ├─ mcp-tools.md
│  ├─ workflow.md
│  └─ style-guidelines.md
└─ scripts/
   ├─ run_diagram_preflight.py
   ├─ optimize_diagram_prompt.py
   ├─ generate_drawio_draft.py
   ├─ generate_visio_script_from_brief.py
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

1. refine rough input into a structured brief
2. retrieve similar diagram references
3. build or edit the draw.io version
4. reconstruct the Visio version
5. verify `.drawio` and `.vsdx`

### `references/input-refinement.md`

Defines the preflight process that:

- tightens user input into a diagram brief
- generates search queries
- retrieves similar reference diagrams before layout
- generates a first draft `.drawio` when needed

### `references/mcp-tools.md`

Explains the tool order for:

- `web.image_query`
- `mcp__drawio__`
- `mcp__visio__`
- PowerShell plus Visio COM

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

### `scripts/optimize_diagram_prompt.py`

Turns rough user input into a structured brief with:

- diagram type
- style guess
- node candidates
- edge-verb hints
- recommended image-search queries

Example:

```bash
python scripts/optimize_diagram_prompt.py "multi-stage 2D 3D registration pipeline for thesis figure"
```

### `scripts/run_diagram_preflight.py`

Runs the local preflight chain end to end and writes:

- `*_brief.json`
- `*_draft.drawio`
- `*_create_visio.ps1`

Example:

```bash
python scripts/run_diagram_preflight.py "multi-stage 2D 3D registration pipeline for thesis figure" --outdir preflight_output --basename registration
```

### `scripts/generate_drawio_draft.py`

Creates a first-pass `.drawio` XML draft from the structured brief generated in preflight.

Example:

```bash
python scripts/generate_drawio_draft.py brief.json draft.drawio
```

### `scripts/generate_visio_script_from_brief.py`

Creates a first-pass PowerShell Visio reconstruction script from the same structured brief.

Example:

```bash
python scripts/generate_visio_script_from_brief.py brief.json create_from_brief.ps1
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
Use $drawio-visio-workflow to optimize a rough process description, retrieve similar reference diagrams, create an academic-style draw.io figure, and deliver both .drawio and .vsdx outputs.
```

## Notes

- This skill treats the `.drawio` file as the structural source of truth.
- For thesis figures, the recommended default style is the academic style in `references/style-guidelines.md`.
- If Windows PowerShell shows garbled Chinese text, rewrite scripts as UTF-8 BOM before execution.
