#!/bin/bash

IMAGE="rredwiz/dalmast:latest"
CONTAINER_NAME="dalmast"

docker build -t "$IMAGE" .

xhost +local:root

# Find the Movella — it usually appears as /dev/ttyUSB0 or /dev/ttyACM0
MOVELLA_DEV="/dev/ttyUSB0"
# this is the permanent symlink for the movella (will not change between ports)
MOVELLA_SYMLINK="/dev/serial/by-id/usb-Xsens_MTi_USB_Converter_DB9K3SNP-if00-port0"

docker run -it \
  --name "$CONTAINER_NAME" \
  --rm \
  -v "$(pwd):/workspace" \
  -w /workspace \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -e ROS_DOMAIN_ID=0 \
  --net=host \
  --device="MOVELLA_SYMLINK" \
  --privileged \
  "$IMAGE"

