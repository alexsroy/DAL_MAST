#!/bin/bash

IMAGE="rredwiz/dalmast:latest"

# only build if image is missing
if ! docker image inspect "$IMAGE" >/dev/null 2>&1; then
    docker build -q -t "$IMAGE" .
fi

docker run -it -v "$(pwd):/workspace" -w /workspace "$IMAGE"
