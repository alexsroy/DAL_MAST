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
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
CMD ["bash"]
