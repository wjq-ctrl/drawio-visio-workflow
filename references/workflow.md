# Workflow

## 1. Inspect the source

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

## 2. Decide the reconstruction level

Choose one of three modes:

- `preserve`: stay close to the original structure and placement
- `optimized`: improve grouping, spacing, and readability
- `academic`: use restrained paper-style grouping and low-saturation colors

For thesis figures, prefer `academic` unless the user asks otherwise.

## 3. Build the Visio script

- Start from `scripts/visio_helpers.ps1`.
- Create a diagram-specific script in the working project, not inside the skill.
- Use the helper functions to draw:
  - containers
  - text labels
  - rectangular processing blocks
  - arrows

Keep the drawing script explicit. Do not attempt a fragile one-shot full auto-layout unless the source is highly regular.

## 4. Generate the Visio file

Typical pattern:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\create_visio_from_drawio_xxx.ps1
```

If PowerShell parsing breaks on Chinese text, rewrite the script as UTF-8 BOM before execution.

## 5. Verify the result

Check:

- `.vsdx` file exists
- path is correct
- file size is non-trivial
- if possible, the layout matches the intended version

Use:

```powershell
Get-Item -LiteralPath '.\figures\example.vsdx' | Select-Object FullName, Length, LastWriteTime
```

## 6. Report clearly

Always report:

- generated file paths
- whether the original draw.io layout was preserved or restyled
- whether any step remained manual
