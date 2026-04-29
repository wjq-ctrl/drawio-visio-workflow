# Workflow

## 1. Preflight the input

When the task begins from description instead of from an existing diagram:

- run `python scripts/optimize_diagram_prompt.py "<raw input>"`
- read the structured brief
- derive similar-image search queries
- run `web.image_query` before locking the first layout
- generate a first draft `.drawio` from the brief when useful

Only after preflight should the diagram move into structural planning.

## 2. Normalize the input

Possible inputs:

- a text description
- a flowchart requirement
- a framework or architecture description
- an image description
- an existing `.drawio`

Before drawing anything, convert the input into:

- node list
- stage or group list
- directed edges
- reading order
- preferred style: `academic`, `optimized`, or `preserve`

If the input is descriptive rather than structural, write a short diagram plan first.
Freeze the main node order before routing arrows.

## 3. Build the draw.io version first

Use `mcp__drawio__` as the primary authoring tool.

If the task starts from description, you may begin from a generated draft `.drawio` created by `scripts/generate_drawio_draft.py`, then refine it in draw.io MCP.

Typical sequence:

1. `start_session`
2. `create_new_diagram` when starting from scratch
3. `get_diagram` before editing an existing diagram
4. `edit_diagram` for iterative refinement
5. `export_diagram` to save the `.drawio`

During draw.io authoring, review arrows explicitly:

- make the main flow direction obvious
- switch to orthogonal routing for data flow
- prevent arrowheads from touching labels
- remove avoidable crossings before export

Reasoning:

- draw.io is better for initial diagram composition
- it is easier to inspect and revise structure there
- the exported `.drawio` becomes the editable intermediate source of truth

## 4. Inspect the source when `.drawio` already exists

- Read the `.drawio` file as UTF-8.
- If labels look garbled in PowerShell, force UTF-8 output or use Python for extraction.
- Run:

```bash
python scripts/extract_drawio_cells.py path/to/file.drawio
```

This produces a JSON summary of:

- vertex cells
- edge cells
- labels
- geometry
- style strings

## 5. Decide the reconstruction level

Choose one of three modes:

- `preserve`: stay close to the original structure and placement
- `optimized`: improve grouping, spacing, and readability
- `academic`: use restrained paper-style grouping and low-saturation colors

For thesis figures, prefer `academic` unless the user asks otherwise.

Apply Huashu-Design discipline here:

- keep the diagram content-first
- use spacing and alignment before adding color
- avoid decorative excess
- make the reading path obvious on first glance
- make data-flow arrows read as a system rather than as individually improvised lines

## 6. Build the Visio version

Choose the Visio path:

- use `mcp__visio__` for simple diagrams with basic rectangles and connectors
- use PowerShell plus Visio COM for more controlled reconstruction

When using PowerShell:

- start from `scripts/visio_helpers.ps1`
- create a diagram-specific script in the working project, not inside the skill
- use the helper functions to draw:
  - containers
  - text labels
  - rectangular processing blocks
  - arrows

Keep the drawing script explicit. Do not attempt a fragile one-shot full auto-layout unless the source is highly regular.
Treat arrow routing as a first-class quality check, not as a final cosmetic pass.

## 7. Generate the Visio file

Typical pattern:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\create_visio_from_drawio_xxx.ps1
```

If PowerShell parsing breaks on Chinese text, rewrite the script as UTF-8 BOM before execution.

## 8. Verify the result

Check:

- `.drawio` file exists
- `.vsdx` file exists
- path is correct
- file size is non-trivial
- if possible, the layout matches the intended version
- data-flow arrows are consistent in direction, weight, spacing, and arrowhead style
- arrow crossings have been minimized
- dashed arrows, if any, are semantically justified

Use:

```powershell
Get-Item -LiteralPath '.\figures\example.vsdx' | Select-Object FullName, Length, LastWriteTime
```

And for draw.io output, verify the exported `.drawio` path as well.

## 9. Report clearly

Always report:

- generated `.drawio` path
- generated `.vsdx` path
- whether the diagram began from description, image description, or existing draw.io
- generated file paths
- whether the diagram was preserved or redesigned
- whether any step remained manual
