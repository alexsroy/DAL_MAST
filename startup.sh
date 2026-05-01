#!/bin/bash

IMAGE="rredwiz/dalmast:latest"
CONTAINER_NAME="dalmast"

docker build -t "$IMAGE" .

xhost +local:root

docker run -it \
  --name "$CONTAINER_NAME" \
  --rm \
  -v "$(pwd):/workspace" \
  -w /workspace \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -e ROS_DOMAIN_ID=0 \
  --net=host \
  "$IMAGE"

