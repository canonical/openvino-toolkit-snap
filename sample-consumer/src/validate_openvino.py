#!/usr/bin/env python3

def main():
    import openvino as ov
    core = ov.Core()
    devices = core.get_available_devices()
    print(f"Supported devices: {devices}")
    import openvino_tokenizers
    import openvino_genai
    print("Successfully imported openvino_tokenizers and openvino_genai")

if __name__ == "__main__":
    main()
