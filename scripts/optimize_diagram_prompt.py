import json
import re
import sys


EDGE_HINTS = [
    "input", "output", "generate", "update", "refine", "optimize", "estimate",
    "predict", "compute", "render", "compare", "fuse", "align", "register",
]

STAGE_PATTERN = re.compile(r"\bstage\s*\d+\b|阶段\s*\d+", re.IGNORECASE)


def normalize_text(text: str) -> str:
    text = text.replace("→", " -> ").replace("=>", " -> ").replace("：", ": ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def split_candidates(text: str):
    chunks = re.split(r"[.;；。,\n]|->|→|\bwith\b|\band\b|\bthen\b", text, flags=re.IGNORECASE)
    return [c.strip(" -") for c in chunks if c.strip(" -")]


def infer_nodes(chunks):
    nodes = []
    seen = set()
    for chunk in chunks:
        simplified = chunk.strip()
        if 2 <= len(simplified) <= 60 and simplified.lower() not in seen:
            if len(simplified.split()) >= 2 or any(k in simplified.lower() for k in ["stage", "registration", "optimization", "input", "output", "drr", "pose"]):
                seen.add(simplified.lower())
                nodes.append(simplified)
    return nodes[:12]


def infer_search_queries(text: str, nodes):
    topic = nodes[0] if nodes else text[:30]
    base = topic.strip()
    return [
        f"{base} flowchart",
        f"{base} pipeline diagram",
        f"{base} framework diagram",
        f"{base} academic figure",
        f"{base} process diagram",
    ]


def infer_edges(nodes):
    edges = []
    for left, right in zip(nodes, nodes[1:]):
        edges.append({"source": left, "target": right, "type": "data_flow"})
    return edges


def infer_stages(nodes):
    stages = []
    for idx, node in enumerate(nodes, start=1):
        match = STAGE_PATTERN.search(node)
        if match:
            stage_name = match.group(0)
        else:
            stage_name = f"Stage {idx}"
        stages.append({"name": stage_name, "nodes": [node]})
    return stages


def infer_style(text: str):
    lowered = text.lower()
    if any(k in lowered for k in ["thesis", "paper", "academic", "论文", "学术"]):
        return "academic"
    if any(k in lowered for k in ["presentation", "slide", "答辩", "汇报"]):
        return "optimized"
    return "optimized"


def infer_diagram_type(text: str):
    lowered = text.lower()
    if "framework" in lowered or "架构" in text or "框架" in text:
        return "framework diagram"
    if "pipeline" in lowered or "流程" in text:
        return "pipeline diagram"
    return "flowchart"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if len(sys.argv) < 2:
        print("Usage: python optimize_diagram_prompt.py <raw text>", file=sys.stderr)
        sys.exit(1)

    raw = " ".join(sys.argv[1:])
    normalized = normalize_text(raw)
    chunks = split_candidates(normalized)
    nodes = infer_nodes(chunks)

    payload = {
        "raw_input": raw,
        "normalized_input": normalized,
        "diagram_type": infer_diagram_type(raw),
        "preferred_style": infer_style(raw),
        "audience_guess": "academic" if infer_style(raw) == "academic" else "general technical",
        "node_candidates": nodes,
        "stages": infer_stages(nodes),
        "edges": infer_edges(nodes),
        "edge_verbs_detected": [w for w in EDGE_HINTS if w in normalized.lower()],
        "recommended_search_queries": infer_search_queries(normalized, nodes),
        "output_contract": [".drawio", ".vsdx"],
    }

    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
