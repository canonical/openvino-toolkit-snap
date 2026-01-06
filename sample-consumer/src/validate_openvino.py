#!/usr/bin/env python3

import argparse
import os
from pathlib import Path

import openvino as ov

print("Successfully imported openvino")
import openvino_genai

print("Successfully imported openvino_genai")


def supported_devices():
    core = ov.Core()
    return core.get_available_devices()


def validate_openvino_genai(model_dir, device="CPU"):
    print(f"\nRunning inference on device: {device}")
    pipe = openvino_genai.LLMPipeline(model_dir, device)
    result = pipe.generate("Why is the sky blue?", max_new_tokens=100)
    print(f"Result: {result}")

    # Validate the result is reasonable
    if not result or len(result.strip()) < 10:
        raise RuntimeError(
            f"Generated text is too short or empty on {device}: '{result}'"
        )

    # Check for common failure patterns
    if result.count(" ") < 3:
        raise RuntimeError(
            f"Generated text appears invalid on {device} (too few words): '{result}'"
        )

    # Check for expected content keywords related to sky color
    result_lower = result.lower()
    required_keywords = ["blue", "light", "water"]
    missing_keywords = [kw for kw in required_keywords if kw not in result_lower]

    if missing_keywords:
        raise RuntimeError(
            f"Generated text on {device} missing expected keywords {missing_keywords}. "
            f"Got: '{result}'"
        )

    print(f"✓ Validation passed for device: {device}")
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Validate OpenVINO with a converted model"
    )
    parser.add_argument(
        "model_name",
        help="HuggingFace model identifier (e.g., 'Qwen/Qwen2.5-3B')",
    )
    parser.add_argument(
        "device",
        choices=["CPU", "GPU", "NPU"],
        help="Device type to run inference on (CPU, GPU, or NPU)",
    )
    args = parser.parse_args()

    # Check if requested device is supported
    devices = supported_devices()
    print(f"Supported devices: {devices}")

    if args.device not in devices:
        raise RuntimeError(
            f"Device '{args.device}' is not supported. Available devices: {devices}"
        )

    # Extract model directory name from model identifier
    model_dir = args.model_name.split("/")[-1] + "-ov"

    # Prepend SNAP_USER_COMMON to model path so snap can read/write under confinement
    snap_user_common = os.environ.get("SNAP_USER_COMMON")
    model_path = str(Path(snap_user_common) / model_dir)

    # Run validation on the specified device
    validate_openvino_genai(model_dir=model_path, device=args.device)
    print(f"\n✓ Validation completed successfully on {args.device}!")



if __name__ == "__main__":
    main()

