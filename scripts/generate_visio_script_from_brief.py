import json
import sys
from pathlib import Path


ACADEMIC_FILL = "234,242,251"
ACADEMIC_LINE = "110,143,179"
OPTIMIZED_FILL = "220,238,254"
OPTIMIZED_LINE = "37,99,235"
ARROW_LINE = "107,114,128"


def load_brief(path: Path):
    for encoding in ("utf-8", "utf-8-sig", "utf-16", "utf-16-le", "utf-16-be"):
        try:
            return json.loads(path.read_text(encoding=encoding))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise ValueError(f"Could not parse JSON brief from {path}")


def ps_string(value: str) -> str:
    return value.replace("'", "''")


def pick_colors(style_name: str):
    if style_name == "academic":
        return ACADEMIC_FILL, ACADEMIC_LINE
    return OPTIMIZED_FILL, OPTIMIZED_LINE


def build_script(brief, output_path: str):
    node_candidates = brief.get("node_candidates") or ["Start", "Process", "Output"]
    style_name = brief.get("preferred_style", "optimized")
    fill_rgb, line_rgb = pick_colors(style_name)

    lines = []
    lines.append("param(")
    lines.append(f"    [string]$OutputPath = '{ps_string(output_path)}'")
    lines.append(")")
    lines.append("")
    lines.append("$ErrorActionPreference = 'Stop'")
    lines.append("$HelperPath = Join-Path $PSScriptRoot '..\\scripts\\visio_helpers.ps1'")
    lines.append("if (!(Test-Path -LiteralPath $HelperPath)) {")
    lines.append("    throw \"visio_helpers.ps1 not found relative to generated script.\"")
    lines.append("}")
    lines.append(". $HelperPath")
    lines.append("")
    lines.append("$Scale = 0.01")
    lines.append("$XOffset = 0.5")
    lines.append("$TopMargin = 0.4")
    lines.append("$PageHeight = 8.5")
    lines.append("")
    lines.append("$visio = New-Object -ComObject Visio.Application")
    lines.append("$visio.Visible = $false")
    lines.append("$doc = $visio.Documents.Add('')")
    lines.append("$page = $visio.ActivePage")
    lines.append("$page.Name = 'GeneratedFromBrief'")
    lines.append("Set-CellFormula $page.PageSheet 'PageWidth' '12 in'")
    lines.append("Set-CellFormula $page.PageSheet 'PageHeight' '8.5 in'")
    lines.append("")

    x = 80
    y = 220
    width = 150
    height = 60
    gap = 70
    centers = []

    for idx, label in enumerate(node_candidates):
        var_name = f"$node{idx + 1}"
        centers.append((x + width, y + height / 2))
        lines.append(
            f"{var_name} = Add-Rect -Page $page -X {x} -Y {y} -Width {width} -Height {height} "
            f"-Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin "
            f"-Text '{ps_string(label)}' -FillRgb '{fill_rgb}' -LineRgb '{line_rgb}' "
            f"-LineWeight '1.1 pt' -FontSize '9 pt'"
        )
        x += width + gap

    lines.append("")

    for idx in range(len(node_candidates) - 1):
        x1 = 80 + idx * (width + gap) + width
        x2 = 80 + (idx + 1) * (width + gap)
        y_mid = y + height / 2
        lines.append(
            f"$null = Add-Arrow -Page $page -X1 {x1} -Y1 {y_mid} -X2 {x2} -Y2 {y_mid} "
            f"-Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin "
            f"-LineRgb '{ARROW_LINE}' -LineWeight '1.1 pt'"
        )

    lines.append("")
    lines.append("$doc.SaveAs($OutputPath)")
    lines.append("$doc.Close()")
    lines.append("$visio.Quit()")
    lines.append("Write-Output \"CREATED: $OutputPath\"")
    lines.append("")
    return "\n".join(lines)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if len(sys.argv) != 3:
        print("Usage: python generate_visio_script_from_brief.py <brief.json> <output.ps1>", file=sys.stderr)
        sys.exit(1)

    brief_path = Path(sys.argv[1])
    output_script = Path(sys.argv[2])
    brief = load_brief(brief_path)
    default_vsdx = str(output_script.with_suffix(".vsdx"))
    content = build_script(brief, default_vsdx)
    output_script.write_text(content, encoding="utf-8")
    print(str(output_script))


if __name__ == "__main__":
    main()
