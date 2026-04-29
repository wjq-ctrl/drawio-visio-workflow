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

## Top-Tier Research Aesthetic

Use this level when the target is close to top journal or top conference figure quality.

- Prefer low-saturation cool palettes over obvious blue-orange contrast.
- Keep the canvas visually quiet. Most of the figure should read as white or near-white.
- Separate stage labels from stage containers. Do not center large titles inside background boxes.
- Use stage containers as structural grouping only, with very light fills and restrained borders.
- Let semantic emphasis come from ordering, alignment, and whitespace before color.
- Avoid visually heavy capsules, badges, shadows, gradients, and icon decoration.
- Use one dominant semantic accent, one supporting neutral, and one output neutral at most.
- Keep node sizes consistent inside the same semantic level.
- Use slightly darker text than borders so labels stay crisp in PDF and print.
- Design for grayscale survivability: if printed without color, the grouping should still be legible.

Recommended palette:

- canvas: `#FFFFFF`
- stage background: `#F7F8FA`
- stage border: `#D6DAE1`
- stage title text: `#344256`
- network block: `#E9F0FB`, border `#5E7BA6`, text `#21324D`
- process block: `#EEF2F6`, border `#72849A`, text `#233548`
- output block: `#F3F4F6`, border `#8D98A8`, text `#2D3642`
- arrows: `#5F6B7A`

Layout guidance:

- stage outer padding: 24 to 32 px
- node-to-node gap inside a row: 56 to 80 px
- stage-to-stage gap: 24 to 40 px
- keep stage titles aligned on a shared baseline
- avoid more than 3 semantic fill colors in one figure

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
