#!/bin/bash

# opens a new shell inside the already-running dalmast service.
# all ROS2 nodes started here share the same network as the main container,
# so topics published by PCBComm will be visible to waypointControl and vice versa.

RUNNING_CONTAINER="$(docker compose -f compose.yaml ps -q --status running dalmast)"

if [ -z "$RUNNING_CONTAINER" ]; then
    echo "Service 'dalmast' is not running. Start it with ./startup.sh first."
    exit 1
fi

docker compose -f compose.yaml exec dalmast bash -lc 'source /opt/ros/jazzy/setup.bash && if [ -f /workspace/install/setup.bash ]; then source /workspace/install/setup.bash; fi && exec bash'
