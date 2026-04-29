# MCP Tools

## Purpose

This skill depends on two MCP tool surfaces:

- `mcp__drawio__` for authoring and exporting `.drawio`
- `mcp__visio__` for basic `.vsdx` reconstruction

It also depends on one search surface before authoring when input is descriptive:

- `web.image_query` for retrieving similar diagram references

Use PowerShell plus Visio COM as the controlled fallback when the Visio MCP surface is not expressive enough.

## Draw.io MCP

Preferred functions:

- `start_session`
- `create_new_diagram`
- `get_diagram`
- `edit_diagram`
- `export_diagram`

Use `create_new_diagram` only when starting from scratch.
Use `get_diagram` before `edit_diagram` when modifying an existing diagram.

Use draw.io MCP for:

- turning a text description into a first diagram draft
- refining grouping and layout
- refining connector routing and arrow consistency
- exporting the final `.drawio`

## Image Search

Use `web.image_query` after prompt refinement and before the first layout pass when the source is:

- text description
- framework description
- image description

Use reference retrieval to calibrate:

- diagram orientation
- grouping density
- connector style
- whitespace and stage treatment

## Visio MCP

Preferred functions:

- `create_visio_file`
- `add_shape`
- `add_text`
- `connect_shapes`
- `list_shapes`

Use Visio MCP for:

- simple block diagrams
- small flowcharts with direct connectors
- quick proof-of-concept reconstruction

Be cautious with arrows in Visio MCP-only flows. If the connector routing starts to look improvised or inconsistent, switch to PowerShell plus Visio COM for tighter control.

## PowerShell plus Visio COM

Use this path when:

- precise positioning matters
- the diagram has grouped stage backgrounds
- you need consistent formatting and custom geometry conversion
- MCP-level Visio operations would be too verbose or too limited

Recommended pattern:

1. inspect the `.drawio`
2. author or refine the diagram in draw.io MCP
3. export `.drawio`
4. create a custom PowerShell script using `scripts/visio_helpers.ps1`
5. execute the script to generate `.vsdx`

## Output Contract

For a complete task, deliver both:

- `.drawio`
- `.vsdx`

Do not stop after only one editable format unless the user explicitly narrows the request.
