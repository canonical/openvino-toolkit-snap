# openvino-toolkit-snap

This is a content producer snap that provides the OpenVINO runtime libraries for consumption by downstream applications. It packages the following components:

- OpenVINO Toolkit
- OpenVINO GenAI
- openVINO Tokenizers

## Sample Python applications

For reference, a sample consumer application using the OpenVINO Python API is provided in the `sample-consumer` folder. This provides an example of how to build a snap package that leverages the OpenVINO runtime and supports the Intel GPU and NPU for inference.