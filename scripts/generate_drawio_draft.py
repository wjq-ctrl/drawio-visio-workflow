import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ACADEMIC_NODE_STYLE = (
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#EAF2FB;"
    "strokeColor=#6E8FB3;strokeWidth=1.2;fontSize=10;fontFamily=Microsoft YaHei;"
)
OPTIMIZED_NODE_STYLE = (
    "rounded=1;whiteSpace=wrap;html=1;fillColor=#DCEEFE;"
    "strokeColor=#2563EB;strokeWidth=1.2;fontSize=10;fontFamily=Microsoft YaHei;"
)
EDGE_STYLE = (
    "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;"
    "html=1;strokeWidth=1.6;strokeColor=#6B7280;endArrow=block;endFill=1;"
)


def load_brief(path: Path):
    for encoding in ("utf-8", "utf-8-sig", "utf-16", "utf-16-le", "utf-16-be"):
        try:
            return json.loads(path.read_text(encoding=encoding))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise ValueError(f"Could not parse JSON brief from {path}")


def pick_node_style(style_name: str):
    return ACADEMIC_NODE_STYLE if style_name == "academic" else OPTIMIZED_NODE_STYLE


def create_cell(root, cell_id, value="", style="", vertex=None, edge=None, parent="1", source=None, target=None, geom=None):
    attrs = {"id": cell_id, "parent": parent}
    if value is not None:
        attrs["value"] = value
    if style:
        attrs["style"] = style
    if vertex is not None:
        attrs["vertex"] = str(vertex)
    if edge is not None:
        attrs["edge"] = str(edge)
    if source:
        attrs["source"] = source
    if target:
        attrs["target"] = target
    cell = ET.SubElement(root, "mxCell", attrs)
    if geom is not None:
        ET.SubElement(cell, "mxGeometry", geom)
    return cell


def build_drawio(brief):
    node_candidates = brief.get("node_candidates") or ["Start", "Process", "Output"]
    style_name = brief.get("preferred_style", "optimized")
    node_style = pick_node_style(style_name)

    mxfile = ET.Element("mxfile", {"host": "Electron", "agent": "Codex", "version": "29.0.3"})
    diagram = ET.SubElement(mxfile, "diagram", {"id": "draft", "name": "Page-1"})
    model = ET.SubElement(
        diagram,
        "mxGraphModel",
        {
            "dx": "1200",
            "dy": "800",
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": "1169",
            "pageHeight": "827",
            "math": "0",
            "shadow": "0",
        },
    )
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

    x = 80
    y = 220
    width = 150
    height = 60
    gap = 70

    node_ids = []
    for idx, label in enumerate(node_candidates, start=2):
        cell_id = f"n{idx}"
        node_ids.append(cell_id)
        create_cell(
            root,
            cell_id,
            value=label,
            style=node_style,
            vertex=1,
            geom={
                "x": str(x),
                "y": str(y),
                "width": str(width),
                "height": str(height),
                "as": "geometry",
            },
        )
        x += width + gap

    edge_index = 1
    for left, right in zip(node_ids, node_ids[1:]):
        create_cell(
            root,
            f"e{edge_index}",
            value="",
            style=EDGE_STYLE,
            edge=1,
            source=left,
            target=right,
            geom={"relative": "1", "as": "geometry"},
        )
        edge_index += 1

    return mxfile


def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_drawio_draft.py <brief.json> <output.drawio>", file=sys.stderr)
        sys.exit(1)

    brief_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    brief = load_brief(brief_path)
    mxfile = build_drawio(brief)
    output_path.write_text(ET.tostring(mxfile, encoding="unicode"), encoding="utf-8")
    print(str(output_path))


if __name__ == "__main__":
    main()
