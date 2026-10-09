cmake_minimum_required(VERSION 3.16)
project(openvino_genai_cmake_check LANGUAGES CXX)

file(GLOB openvino_configs
    "$ENV{OPENVINO_SNAP}/usr/lib/${CMAKE_LIBRARY_ARCHITECTURE}/cmake/openvino*/OpenVINOConfig.cmake")
list(LENGTH openvino_configs config_count)
if(NOT config_count EQUAL 1)
    message(FATAL_ERROR "Expected one OpenVINO CMake config in $ENV{OPENVINO_SNAP}, found ${config_count}")
endif()
get_filename_component(OpenVINO_DIR "${openvino_configs}" DIRECTORY)

find_package(OpenVINOGenAI CONFIG REQUIRED
    PATHS "$ENV{OPENVINO_SNAP}/usr/runtime/cmake" NO_DEFAULT_PATH)
if(NOT TARGET openvino::genai OR NOT TARGET openvino::genai::c)
    message(FATAL_ERROR "OpenVINO GenAI C and C++ targets are required")
endif()

install(CODE "")