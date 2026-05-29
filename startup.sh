#!/bin/bash
set -e

MOVELLA_SYMLINK="/dev/serial/by-id/usb-Xsens_MTi_USB_Converter_DB9K3SNP-if00-port0"
PCB_SERIAL_PORT="/dev/ttyS0"
MODE="${1:-auto}"

COMPOSE_FILES=(-f compose.yaml)

if [ "$MODE" = "pi" ]; then
  COMPOSE_FILES+=(-f compose.pi.yaml)
elif [ "$MODE" = "auto" ] && [ -e "$MOVELLA_SYMLINK" ] && [ -e "$PCB_SERIAL_PORT" ]; then
  COMPOSE_FILES+=(-f compose.pi.yaml)
elif [ "$MODE" != "auto" ] && [ "$MODE" != "dev" ]; then
  echo "Usage: ./startup.sh [auto|dev|pi]"
  exit 1
fi

xhost +local:root >/dev/null 2>&1 || true

RUNNING_CONTAINER="$(docker compose "${COMPOSE_FILES[@]}" ps -q --status running dalmast)"

docker compose "${COMPOSE_FILES[@]}" up -d --build

if [ -z "$RUNNING_CONTAINER" ]; then
  docker compose "${COMPOSE_FILES[@]}" exec dalmast bash -lc \
    'source /opt/ros/jazzy/setup.bash && colcon build'
fi

docker compose "${COMPOSE_FILES[@]}" exec dalmast bash -lc \
  'source /opt/ros/jazzy/setup.bash && if [ -f /workspace/install/setup.bash ]; then source /workspace/install/setup.bash; fi && exec bash'
