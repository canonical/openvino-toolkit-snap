import openvino as ov

core = ov.Core()
devices = core.get_available_devices()

print(f"Supported devices: {devices}")
