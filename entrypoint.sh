#!/bin/bash
set -e

source "/opt/ros/jazzy/setup.bash"

# check if the workspace has been built yet
if [ ! -f "/workspace/install/setup.bash" ]; then
    echo "building workspace..."
    colcon build
else
    echo "build files already found, skipping build."
fi

source "/workspace/install/setup.bash"

echo "mast docker container is ready."
exec "$@"
