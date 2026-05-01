#!/bin/bash

IMAGE="rredwiz/dalmast:latest"
CONTAINER_NAME="dalmast"

docker build -t "$IMAGE" .

xhost +local:root

# Find the Movella — it usually appears as /dev/ttyUSB0 or /dev/ttyACM0
MOVELLA_DEV="/dev/ttyUSB0"

docker run -it \
  --name "$CONTAINER_NAME" \
  --rm \
  -v "$(pwd):/workspace" \
  -w /workspace \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -e ROS_DOMAIN_ID=0 \
  --net=host \
  --device="$MOVELLA_DEV" \
  --privileged \
  "$IMAGE"

