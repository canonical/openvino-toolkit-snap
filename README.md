# openvino-toolkit-snap

This is a content producer snap that provides the OpenVINO runtime libraries for consumption by downstream applications.

## Example `snapcraft.yaml` for consuming applications

An example snippet for a consuming app's `snapcraft.yaml` might look like the following:

```yaml
plugs:
  openvino-libs:
    interface: content
    content: openvino-libs-2404
    target: $SNAP/openvino

environment:
  LD_LIBRARY_PATH: $SNAP/openvino:$LD_LIBRARY_PATH

apps:
  openvino-enabled-app:
    command: ...
    plugs:
      - openvino-libs
```
