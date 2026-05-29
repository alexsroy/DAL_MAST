#!/bin/bash
set -e

source "/opt/ros/jazzy/setup.bash"

echo "mast docker container is ready."
exec "$@"
