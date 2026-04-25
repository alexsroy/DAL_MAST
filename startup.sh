#!/bin/bash

IMAGE="rredwiz/dalmast:latest"

docker build -t "$IMAGE" .

xhost +local:root

docker run -it \
  -v "$(pwd):/workspace" \
  -w /workspace \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  --net=host \
  "$IMAGE"

