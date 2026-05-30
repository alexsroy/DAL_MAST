#!/bin/bash
set -e

# opens a new shell inside the already-running dalmast service.
# all ROS2 nodes started here share the same network as the main container,
# so topics published by PCBComm will be visible to waypointControl and vice versa.

MODE="${1:-auto}"

source "$(dirname "$0")/docker_common.sh"
compose_files_for_mode "$MODE"

RUNNING_CONTAINER="$(docker compose "${COMPOSE_FILES[@]}" ps -q --status running dalmast)"

if [ -z "$RUNNING_CONTAINER" ]; then
    echo "Service 'dalmast' is not running. Start it with ./startup.sh ${MODE} first."
    exit 1
fi

enter_dalmast_shell
