#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path


def download_and_convert_model(model_name, output_path):
    """
    Download model and convert it to OpenVINO IR format using optimum-cli.

    Args:
        model_name: HuggingFace model identifier
        output_path: Full output path for converted model

    Returns:
        Path to the converted model directory
    """
    output_path = Path(output_path)

    # Check if model already exists
    if output_path.exists() and any(output_path.iterdir()):
        print(f"Model already exists at {output_path}")
        return str(output_path)

    print(f"Downloading and converting {model_name} to OpenVINO IR format...")

    try:
        # Use optimum-cli to export the model to OpenVINO format
        cmd = [
            "optimum-cli",
            "export",
            "openvino",
            "--model",
            model_name,
            "--trust-remote-code",
            str(output_path),
        ]

        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)

        print(f"Successfully converted model to {output_path}")
        return str(output_path)

    except subprocess.CalledProcessError as e:
        print(f"Error during model conversion: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: optimum-cli not found. Please install optimum[openvino]")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Download and convert a HuggingFace model to OpenVINO IR format"
    )
    parser.add_argument(
        "model_name",
        help="HuggingFace model identifier (e.g., 'Qwen/Qwen2.5-3B')",
    )
    args = parser.parse_args()

    # Extract model directory name from model identifier
    model_dir = args.model_name.split("/")[-1] + "-ov"

    # Prepend SNAP_USER_COMMON to model path so snap can read/write under confinement
    snap_user_common = os.environ.get("SNAP_USER_COMMON")
    model_path = str(Path(snap_user_common) / model_dir)

    download_and_convert_model(args.model_name, model_path)
    print(f"\nModel converted successfully to: {model_path}")


if __name__ == "__main__":
    main()
