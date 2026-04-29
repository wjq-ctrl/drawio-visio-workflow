import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_cell(cell):
    geom = cell.find("mxGeometry")
    geometry = {}
    if geom is not None:
        for key in ("x", "y", "width", "height", "relative", "as"):
            if key in geom.attrib:
                geometry[key] = geom.attrib[key]

    return {
        "id": cell.attrib.get("id"),
        "value": cell.attrib.get("value", ""),
        "style": cell.attrib.get("style", ""),
        "parent": cell.attrib.get("parent"),
        "vertex": cell.attrib.get("vertex"),
        "edge": cell.attrib.get("edge"),
        "source": cell.attrib.get("source"),
        "target": cell.attrib.get("target"),
        "geometry": geometry,
    }


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if len(sys.argv) != 2:
        print("Usage: python extract_drawio_cells.py <file.drawio>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    tree = ET.parse(path)
    root = tree.getroot()

    cells = []
    for cell in root.findall(".//mxCell"):
        cells.append(parse_cell(cell))

    vertices = [c for c in cells if c["vertex"] == "1"]
    edges = [c for c in cells if c["edge"] == "1"]

    payload = {
        "file": str(path),
        "total_cells": len(cells),
        "vertex_count": len(vertices),
        "edge_count": len(edges),
        "vertices": vertices,
        "edges": edges,
    }

    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
