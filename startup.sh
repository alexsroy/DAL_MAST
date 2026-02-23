#!/bin/bash

IMAGE="rredwiz/dalmast:latest"

docker build --platform linux/amd64 -t "$IMAGE" .
docker run -it -v "$(pwd):/workspace" -w /workspace "$IMAGE"
