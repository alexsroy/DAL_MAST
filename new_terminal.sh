#!/bin/bash

# opens a new shell inside the already-running dalmast container.
# all ROS2 nodes started here share the same network as the main container,
# so topics published by PCBComm will be visible to waypointControl and vice versa.

CONTAINER_NAME="dalmast"

if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "Container '${CONTAINER_NAME}' is not running. Start it with ./startup.sh first."
    exit 1
fi

docker exec -it "$CONTAINER_NAME" bash -c 'source /opt/ros/jazzy/setup.bash && source /workspace/install/setup.bash && bash'
