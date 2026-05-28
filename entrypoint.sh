#!/bin/bash
set -e

source "/opt/ros/jazzy/setup.bash"

echo "building workspace..."
colcon build

source "/workspace/install/setup.bash"

echo "mast docker container is ready."
exec "$@"
