import argparse
import os
import json
import subprocess
import sys
from pathlib import Path


def run_command(args):
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(args, capture_output=True, env=env)
    stdout = result.stdout.decode("utf-8", errors="replace").strip()
    stderr = result.stderr.decode("utf-8", errors="replace").strip()
    if result.returncode != 0:
        raise RuntimeError(stderr or f"Command failed: {' '.join(args)}")
    return stdout


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Run the full local diagram pipeline from raw input to brief, draft drawio, Visio script, and final vsdx."
    )
    parser.add_argument("raw_input", help="Raw text description for the target diagram.")
    parser.add_argument("--outdir", default="pipeline_output", help="Output directory for generated artifacts.")
    parser.add_argument("--basename", default="diagram", help="Base file name for generated artifacts.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    outdir = Path(args.outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    preflight_script = root / "run_diagram_preflight.py"

    preflight_raw = run_command(
        [sys.executable, str(preflight_script), args.raw_input, "--outdir", str(outdir), "--basename", args.basename]
    )
    payload = json.loads(preflight_raw)

    visio_script = Path(payload["visio_script"])
    visio_output = visio_script.with_suffix(".vsdx")

    run_command(
        [
            "powershell",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(visio_script),
            "-OutputPath",
            str(visio_output),
        ]
    )

    payload["visio_output"] = str(visio_output)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
