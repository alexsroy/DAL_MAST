#!/bin/bash
set -e

MODE="${1:-auto}"

source "$(dirname "$0")/docker_common.sh"
compose_files_for_mode "$MODE"

xhost +local:root >/dev/null 2>&1 || true

RUNNING_CONTAINER="$(docker compose "${COMPOSE_FILES[@]}" ps -q --status running dalmast)"

docker compose "${COMPOSE_FILES[@]}" up -d --build

if [ -z "$RUNNING_CONTAINER" ]; then
  docker compose "${COMPOSE_FILES[@]}" exec dalmast bash -lc \
    'source /opt/ros/jazzy/setup.bash && colcon build'
fi

enter_dalmast_shell
