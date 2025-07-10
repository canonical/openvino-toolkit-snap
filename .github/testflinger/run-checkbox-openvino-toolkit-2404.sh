#!/bin/bash -e

sudo usermod -a -G render ubuntu
# Newer versions of Ubuntu ship Udev rules which handle this,
# but 22.04 does not
sudo chown root:render /dev/accel/accel0
sudo chmod g+rw /dev/accel/accel0

sudo checkbox-openvino-toolkit-2404.install-full-deps

echo
echo "=== Checkbox OpenVINO Toolkit 2404 ==="
echo "========= DEVICE KERNEL INFO ========="
echo
uname -a
echo
echo "======================================"
echo

checkbox-openvino-toolkit-2404.test-runner-automated
