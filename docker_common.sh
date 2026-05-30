#!/bin/bash

MOVELLA_SYMLINK="/dev/serial/by-id/usb-Xsens_MTi_USB_Converter_DB9K3SNP-if00-port0"
PCB_SERIAL_PORT="/dev/ttyS0"

compose_files_for_mode() {
  local mode="${1:-auto}"

  COMPOSE_FILES=(-f compose.yaml)

  if [ "$mode" = "pi" ]; then
    COMPOSE_FILES+=(-f compose.pi.yaml)
  elif [ "$mode" = "auto" ] && [ -e "$MOVELLA_SYMLINK" ] && [ -e "$PCB_SERIAL_PORT" ]; then
    COMPOSE_FILES+=(-f compose.pi.yaml)
  elif [ "$mode" != "auto" ] && [ "$mode" != "dev" ]; then
    echo "Usage: $0 [auto|dev|pi]"
    exit 1
  fi
}

enter_dalmast_shell() {
  docker compose "${COMPOSE_FILES[@]}" exec dalmast bash -lc \
    'source /opt/ros/jazzy/setup.bash && if [ -f /workspace/install/setup.bash ]; then source /workspace/install/setup.bash; fi && exec bash'
}
