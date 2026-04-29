# Input Refinement

Use this process when the user starts from description instead of from an existing diagram file.

## Goal

Turn rough input into:

- a cleaner diagram brief
- a first-pass node and edge structure
- search queries for similar reference diagrams

## Step 1. Tighten the prompt

Rewrite the raw input into a structured brief with:

- diagram type
- subject
- target audience
- mandatory nodes
- optional nodes
- mandatory edge directions
- stage grouping
- preferred style
- output requirement: `.drawio` plus `.vsdx`

Use `scripts/optimize_diagram_prompt.py` to generate a first-pass structured brief.

## Step 2. Generate reference-search queries

Before drawing, derive 3 to 6 image queries.

Good query patterns:

- `<topic> flowchart`
- `<topic> pipeline diagram`
- `<topic> framework diagram`
- `<topic> academic figure`
- `<topic> system architecture diagram`
- `<topic> process diagram`

If the user specifies thesis or paper use, include `academic figure` or `paper diagram` in at least one query.

## Step 3. Retrieve similar images

Use `web.image_query` to retrieve similar diagrams and inspect them for:

- flow direction
- node density
- stage grouping
- arrow routing
- title treatment
- whitespace level

Do not copy a reference diagram literally. Use references to calibrate composition and readability.

## Step 4. Convert references into a drawing plan

After reference search, decide:

- left-to-right or top-to-bottom
- how many major groups or stages
- how many nodes are necessary
- whether side input/output panels are useful
- what arrow style should be consistent across the figure

Only after these decisions should you begin draw.io authoring.

## Step 5. Generate a draft draw.io file

After the brief is stable, generate a first draft `.drawio`:

```bash
python scripts/generate_drawio_draft.py brief.json output.drawio
```

This draft is not the final figure. It is the first structured layout pass that can then be refined with draw.io MCP.

## Step 6. Generate a first-pass Visio script

When the brief is regular enough for direct automation, generate a PowerShell reconstruction script:

```bash
python scripts/generate_visio_script_from_brief.py brief.json create_from_brief.ps1
```

This creates a first-pass Visio script that:

- references `scripts/visio_helpers.ps1`
- lays out nodes in a consistent left-to-right row
- draws standardized data-flow arrows
- saves a `.vsdx`

Use it as a scaffold, not as the final guarantee of quality.
