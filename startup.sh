#!/bin/bash
set -e

IMAGE="rredwiz/dalmast:latest"
CONTAINER_NAME="dalmast"

MOVELLA_SYMLINK="/dev/serial/by-id/usb-Xsens_MTi_USB_Converter_DB9K3SNP-if00-port0"
PCB_SERIAL_PORT="/dev/ttyS0"

DOCKER_DEVICES=()

if [ -e "$MOVELLA_SYMLINK" ]; then
  DOCKER_DEVICES+=(--device="$MOVELLA_SYMLINK:/dev/ttyUSB0")
else
  echo "Movella device not found; continuing without it."
fi

if [ -e "$PCB_SERIAL_PORT" ]; then
  DOCKER_DEVICES+=(--device="$PCB_SERIAL_PORT:/dev/ttyS0")
else
  echo "PCB serial port not found; continuing without it."
fi

docker build -t "$IMAGE" .

xhost +local:root

docker run -it \
  --name "$CONTAINER_NAME" \
  --rm \
  -v "$(pwd):/workspace" \
  -w /workspace \
  -e DISPLAY="$DISPLAY" \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -e ROS_DOMAIN_ID=0 \
  --net=host \
  "${DOCKER_DEVICES[@]}" \
  --privileged \
  "$IMAGE"
