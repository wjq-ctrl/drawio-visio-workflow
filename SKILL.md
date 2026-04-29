---
name: drawio-visio-workflow
description: Inspect draw.io (.drawio) diagram files, extract their structure, and rebuild them as editable Microsoft Visio (.vsdx) diagrams through a repeatable workflow. Use when Codex needs to analyze a draw.io file, restyle a flowchart, reproduce a diagram in Visio, or automate draw.io-to-Visio conversion with PowerShell and Visio COM.
---

# Drawio Visio Workflow

Use this skill when the source of truth is a `.drawio` file and the deliverable needs to be an editable `.vsdx`.

## Workflow

1. Read the source `.drawio` file as UTF-8.
2. Extract cells, labels, geometry, and edges with `scripts/extract_drawio_cells.py`.
3. Decide the target style before editing:
   - Preserve original layout
   - Optimize layout for presentation
   - Restyle for academic paper figures
4. Rebuild the diagram in Visio with PowerShell and Visio COM.
5. Save the `.vsdx` next to the source figure unless the user asks for another path.
6. Verify that the output file exists and report the generated paths.

## Operating Rules

- Treat the `.drawio` file as the structural source. Do not guess labels or topology when the file already defines them.
- Prefer restrained styling for thesis and paper figures: light background, limited palette, consistent line weights, and explicit stage grouping.
- Keep reusable Visio drawing helpers in `scripts/visio_helpers.ps1` and create per-diagram scripts that call those helpers.
- If the console shows garbled Chinese text, re-read the file as UTF-8 or write scripts back with UTF-8 BOM before executing them in Windows PowerShell.
- When a diagram is too bespoke for full automation, still automate extraction and helper functions, then script the final placement manually.

## Files To Read

- Read [references/workflow.md](references/workflow.md) for the end-to-end procedure and decision points.
- Read [references/style-guidelines.md](references/style-guidelines.md) when the user asks for academic, presentation, or neutral visual treatment.
- Use [scripts/extract_drawio_cells.py](scripts/extract_drawio_cells.py) to inspect the `.drawio` structure.
- Reuse [scripts/visio_helpers.ps1](scripts/visio_helpers.ps1) when creating a Visio reconstruction script.

## Typical Requests

- "Convert this draw.io diagram to Visio."
- "Redraw this draw.io flowchart in academic paper style and export .vsdx."
- "Analyze the draw.io structure first, then generate an editable Visio file."
- "Turn this existing draw.io figure into an editable Visio version."

## Output Pattern

For each task, produce:

1. The generated `.vsdx` file.
2. Any new `.drawio` variant if the layout or style changed.
3. The PowerShell reconstruction script when custom Visio drawing logic was needed.
4. A short summary of what was preserved, what was restyled, and what remains manual.
