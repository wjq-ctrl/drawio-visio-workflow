import argparse
import json
import subprocess
import sys
from pathlib import Path


def run_command(args):
    result = subprocess.run(args, capture_output=True)
    stdout = result.stdout.decode("utf-8", errors="replace").strip()
    stderr = result.stderr.decode("utf-8", errors="replace").strip()
    if result.returncode != 0:
        raise RuntimeError(stderr or f"Command failed: {' '.join(args)}")
    return stdout


def write_json(path: Path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Run the local preflight pipeline from raw description to brief, draft drawio, and Visio script."
    )
    parser.add_argument("raw_input", help="Raw text description for the target diagram.")
    parser.add_argument("--outdir", default="preflight_output", help="Output directory for generated artifacts.")
    parser.add_argument("--basename", default="diagram", help="Base file name for generated artifacts.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    outdir = Path(args.outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    brief_path = outdir / f"{args.basename}_brief.json"
    drawio_path = outdir / f"{args.basename}_draft.drawio"
    visio_script_path = outdir / f"{args.basename}_create_visio.ps1"

    optimize_script = root / "optimize_diagram_prompt.py"
    drawio_script = root / "generate_drawio_draft.py"
    visio_script = root / "generate_visio_script_from_brief.py"

    optimized_raw = run_command([sys.executable, str(optimize_script), args.raw_input])
    brief = json.loads(optimized_raw)
    write_json(brief_path, brief)

    run_command([sys.executable, str(drawio_script), str(brief_path), str(drawio_path)])
    run_command([sys.executable, str(visio_script), str(brief_path), str(visio_script_path)])

    payload = {
        "raw_input": args.raw_input,
        "brief_json": str(brief_path),
        "drawio_draft": str(drawio_path),
        "visio_script": str(visio_script_path),
        "recommended_search_queries": brief.get("recommended_search_queries", []),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
