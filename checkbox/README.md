# Checkbox Provider for OpenVINO Toolkit 2404 Snap

This directory contains the Checkbox OpenVINO Toolkit 2404 Provider, including the snap recipe for building the snap and integrating with the Checkbox snap. The test plan integrates with the OpenVINO Python API.

## Installation

Prerequisites:

```
sudo snap install --classic snapcraft
sudo snap install checkbox24
sudo snap install lxd
sudo adduser ubuntu lxd
lxd init --auto
```

Now build and install the sample content consumer snap and the checkbox provider for OpenVINO Toolkit 2404:

```
git clone -b openvino-toolkit-2404 https://github.com/canonical/openvino-toolkit-snap.git

# first build and install content consumer snap and install it
cd openvino-toolkit-snap/sample-consumer
snapcraft
sudo snap install --dangerous ./openvino-sample-consumer_1.0.0_amd64.snap

# now build and install the checkbox tests for openvino-toolkit-2404
cd ../openvino-toolkit-snap/checkbox
snapcraft
sudo snap install --dangerous --classic ./checkbox-openvino-toolkit-2404_1.0.0_amd64.snap
```

## Installing test dependencies

```
checkbox-openvino-toolkit-2404.install-full-deps
```

By default, `checkbox-openvino-toolkit-2404.install-full-deps` will NOT install the `openvino-toolkit-2404` snap. This is by design as typically tests will be run on a modified version of the snap built and installed locally. To install the latest version from the `latest/stable` channel in the Snap Store use:

```
checkbox-openvino-toolkit-2404.install-full-deps --install_from_store
```

## Automated run

```
checkbox-openvino-toolkit-2404.test-runner-automated
```

## Manual run

```
checkbox-openvino-toolkit-2404.test-runner
```
