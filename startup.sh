#!/bin/bash

IMAGE="rredwiz/dalmast:latest"

docker build -t "$IMAGE" .

xhost +local:root

# Find the Movella — it usually appears as /dev/ttyUSB0 or /dev/ttyACM0
MOVELLA_DEV="/dev/ttyUSB0"

docker run -it \
  -v "$(pwd):/workspace" \
  -w /workspace \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  --net=host \
  --device="$MOVELLA_DEV" \
  --privileged \
  "$IMAGE"

