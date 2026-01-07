# Sample content consumer app for `openvino-toolkit-2404`

## Building

```
snapcraft pack
```

## Installing

```
sudo snap install --dangerous ./openvino-sample-consumer_1.0.0_amd64.snap
```

If you have not already, also install the `openvino-toolkit-2404` and `intel-npu-driver` snaps. The first is required while the second is optional for machines containing an Intel NPU, which is an AI inference accelerator built into Intel Core Ultra CPUs starting with Meteor Lake.

```
sudo snap install openvino-toolkit-2404 # required
sudo snap install intel-npu-driver # optional
```

## Connecting snapd interfaces

All snapd interfaces should auto-connect (based on global settings in the store), but if not you can manually connect like so:

```
sudo snap connect openvino-sample-consumer:npu-libs intel-npu-driver:npu-libs
sudo snap connect openvino-sample-consumer:openvino-libs openvino-toolkit-2404:openvino-libs
sudo snap connect openvino-sample-consumer:intel-npu intel-npu-driver:intel-npu-plug
sudo snap connect openvino-sample-consumer:opengl
```