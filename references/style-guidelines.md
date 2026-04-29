# Style Guidelines

These guidelines should be applied with Huashu-Design judgment:

- derive the composition from the information flow
- make grouping and hierarchy legible before adding stylistic contrast
- avoid decorative icons, gradients, and unnecessary chrome unless the content truly benefits
- prefer a diagram that reads clearly in a thesis PDF over one that only looks lively on screen

## Academic

Use this for thesis, paper, and formal report figures.

- Prefer white or near-white canvas
- Use light gray stage bands
- Use one muted blue for network modules
- Use one blue-gray or gray for processing modules
- Use one neutral gray for outputs
- Avoid rounded badges, heavy shadows, bright accents, and decorative icons
- Keep line weights consistent
- Align blocks to a clean grid
- Keep stage titles modest and formal
- Use color as a semantic aid, not as the main source of visual interest
- Use orthogonal data-flow arrows by default unless the content truly requires another path

Recommended palette:

- canvas: `#FFFFFF`
- stage background: `#FBFCFD`
- stage border: `#C7CDD8`
- network block: `#EAF2FB`, border `#6E8FB3`
- process block: `#F1F5F9`, border `#7D8FA3`
- output block: `#F6F7F9`, border `#9AA4B2`
- arrows: `#6B7280`

### Data-Flow Arrow Rules

Apply these rules to both `.drawio` and `.vsdx` outputs:

- Use a single arrow direction for the main reading flow, usually left to right.
- Use orthogonal connectors by default. Avoid casual diagonals.
- Keep arrow line weight consistent across the figure.
- Use the same arrowhead style for all normal data-flow edges.
- Connect from the side that matches the reading flow:
  - left or right sides for left-to-right flow
  - top or bottom only when the structure requires vertical progression
- Avoid arrow crossings whenever possible. Reposition nodes before accepting cluttered crossings.
- Keep enough spacing between parallel arrows so they do not visually merge.
- Do not let arrowheads overlap text, borders, or nearby boxes.
- Use dashed arrows only for secondary semantics such as feedback, optional flow, or reference links.
- If a diagram contains both control flow and data flow, keep them visually distinct by dash pattern or color, but do not introduce a large color system just for arrows.

## Optimized Presentation

Use this when the user wants clearer grouping or a cleaner presentation but not a fully academic paper look.

- Keep side panels for input and output
- Use slightly stronger separation between stage titles and content
- Allow a small amount of color coding
- Preserve the reading order left to right
- Keep enough whitespace so the flow is scannable at presentation distance
- Keep connectors cleaner than the source version even when preserving most box geometry

## Preserve Original

Use this when fidelity matters more than redesign.

- Keep original geometry wherever practical
- Keep original labels verbatim
- Only normalize elements that Visio cannot represent cleanly

## Starting from Description

When the source is not an existing diagram:

- identify the minimum set of nodes needed to explain the process
- avoid over-fragmenting one idea into too many boxes
- keep the edge flow directional and unambiguous
- choose stage grouping only when it clarifies progression or module boundaries
- route arrows only after the node order is stable
