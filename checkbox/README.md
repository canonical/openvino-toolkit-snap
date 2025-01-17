# Checkbox Provider for OpenVINO Toolkit 2404 Snap

This directory contains the Checkbox OpenVINO Toolkit 2404 Provider, including the snap recipe for building the snap and integrating with the Checkbox snap. The test plan integrates with the OpenVINO Python API.

## Installation

Prerequisites:

```
sudo snap install --classic snapcraft
sudo snap install checkbox22
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

Among the dependencies that are installed is the `openvino-ai-plugins-gimp` snap from the store. Snapd interfaces are also manually connected where required.

By default, `checkbox-openvino-toolkit-2404.install-full-deps` will NOT install the `openvino-toolkit-2404` snap. This is by design as typically tests will be run on a modified version of the snap built and installed locally. To install the latest version from the `latest/beta` channel in the Snap Store use:

```
checkbox-openvino-toolkit-2404.install-full-deps --install_from_store
```

Note that the checkbox tests will install models to the same path(s) used by the `openvino-ai-plugins-gimp.model-setup` application. This is because the application has permissions to only write to certain paths, and thus users are not allowed the flexibility to install to any arbitrary path. Therefore, in order for the GIMP plugin tests to run, the models and a config file should be absent in order to test whether the application creates these files in the expected locations. Between checkbox runs, you can remove these files and directories by passing the `--clean_plugin_dirs` option:

```
checkbox-openvino-toolkit-2404.install-full-deps --clean_plugin_dirs
```

**IMPORTANT**: please use this with caution as it will remove models that you may have previously installed to a machine for running the OpenVINO AI plugins with GIMP.

## Automated run

```
checkbox-openvino-toolkit-2404.test-runner-automated
```

## Manual run

```
checkbox-openvino-toolkit-2404.test-runner
```
