FROM ros:jazzy-ros-core

RUN apt-get update && apt-get install -y \
    build-essential \
    vim \
    python3-colcon-common-extensions \
    python3-pygame \
    python3-serial \
    ros-jazzy-turtlesim \
    glpk-utils \
    nano \
    ros-jazzy-xacro \
    ros-jazzy-robot-state-publisher \
    libudev-dev \
    ros-jazzy-nmea-msgs \
    ros-jazzy-nmea-msgs \
    ros-jazzy-mavros-msgs \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

WORKDIR /workspace
CMD ["bash"]
