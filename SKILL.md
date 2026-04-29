---
name: drawio-visio-workflow
description: Create flowcharts, framework diagrams, and process diagrams from a user description, image description, or existing draw.io file, then deliver both editable draw.io (.drawio) and Microsoft Visio (.vsdx) outputs through a repeatable workflow. Use when Codex needs to design a diagram, restyle a diagram for thesis or presentation use, reconstruct a draw.io file in Visio, or automate draw.io-to-Visio delivery with draw.io MCP, Visio tools, and PowerShell plus Visio COM.
---

# Drawio Visio Workflow

Use this skill when the input is:

- a text description of a flowchart
- a framework or pipeline description
- an image or image description that needs to become a structured diagram
- an existing `.drawio` file

and the output needs to include both:

- an editable `.drawio`
- an editable `.vsdx`

## Workflow

1. Normalize the input into a diagram plan:
   - identify nodes
   - identify groups or stages
   - identify directed edges
   - identify the intended visual style
2. Create or edit the diagram in draw.io first.
3. Export or save the `.drawio` file.
4. Rebuild the same structure in Visio.
5. Save the `.vsdx` next to the `.drawio` unless the user asks for another path.
6. Verify both output files and report the generated paths.

## Required Tooling

Prefer this tool order:

1. `mcp__drawio__`
   - `start_session`
   - `create_new_diagram`
   - `get_diagram`
   - `edit_diagram`
   - `export_diagram`
2. `mcp__visio__` when the diagram is simple enough for shape-by-shape reconstruction
3. PowerShell + Visio COM when the Visio tool surface is too limited for the target diagram

Use draw.io as the primary authoring surface. Use Visio as the delivery reconstruction surface.

## Operating Rules

- When starting from description instead of an existing file, define the diagram structure explicitly before drawing.
- Treat the `.drawio` file as the structural source whenever one already exists. Do not guess labels or topology when the file already defines them.
- Apply Huashu-Design discipline to the visual result:
  - design from the content, not from decoration
  - keep information hierarchy clearer than ornament
  - prefer clean grouping, spacing, and alignment over effects
- Prefer restrained styling for thesis and paper figures: light background, limited palette, consistent line weights, and explicit stage grouping.
- Keep reusable Visio drawing helpers in `scripts/visio_helpers.ps1` and create per-diagram scripts that call those helpers.
- If the console shows garbled Chinese text, re-read the file as UTF-8 or write scripts back with UTF-8 BOM before executing them in Windows PowerShell.
- When a diagram is too bespoke for full automation, still automate structure extraction and helper functions, then script the final placement manually.

## Files To Read

- Read [references/workflow.md](references/workflow.md) for the end-to-end procedure and decision points.
- Read [references/style-guidelines.md](references/style-guidelines.md) when the user asks for academic, presentation, or neutral visual treatment.
- Read [references/mcp-tools.md](references/mcp-tools.md) for the exact MCP responsibilities and tool ordering.
- Use [scripts/extract_drawio_cells.py](scripts/extract_drawio_cells.py) to inspect the `.drawio` structure.
- Reuse [scripts/visio_helpers.ps1](scripts/visio_helpers.ps1) when creating a Visio reconstruction script.

## Typical Requests

- "Create a flowchart from this process description and export both draw.io and Visio."
- "Turn this framework description into a thesis-style diagram."
- "Use this image description to draw a structured pipeline figure."
- "Convert this draw.io diagram to Visio."
- "Redraw this draw.io flowchart in academic paper style and export .vsdx."
- "Analyze the draw.io structure first, then generate an editable Visio file."
- "Turn this existing draw.io figure into an editable Visio version."

## Output Pattern

For each task, produce:

1. The generated `.drawio` file.
2. The generated `.vsdx` file.
3. Any diagram-specific PowerShell reconstruction script when custom Visio drawing logic was needed.
4. A short summary of the source input, structure decisions, style decisions, and any remaining manual limitations.
