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

apps:
  openvino-enabled-app:
    command-chain: ["command-chain/openvino-launch"]
    command: ...
    plugs:
      - openvino-libs

parts:
  ...
  command-chain-openvino:
    plugin: dump
    source-type: git
    source: https://github.com/canonical/openvino-toolkit-snap.git
    source-tag: 2024.5.0-0
    stage:
      - command-chain/openvino-launch
```
