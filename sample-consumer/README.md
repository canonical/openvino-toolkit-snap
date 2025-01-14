# Sample content consumer app for openvino-toolkit-2404

## Building

```
snapcraft
```

## Installing

```
sudo snap install --dangerous ./openvino-sample-consumer_1.0.0_amd64.snap
```

## Connecting snapd interfaces

```
sudo snap connect openvino-sample-consumer:npu-libs intel-npu-driver:npu-libs
sudo snap connect openvino-sample-consumer:openvino-libs openvino-toolkit-2404:openvino-libs
```

The following should autoconnect:

```
sudo snap connect openvino-sample-consumer:intel-npu intel-npu-driver:intel-npu-plug
sudo snap connect openvino-sample-consumer:opengl
```