#!/bin/bash

IMAGE="rredwiz/dalmast:latest"

docker build -t "$IMAGE" .
docker run -it -v "$(pwd):/workspace" -w /workspace "$IMAGE"
