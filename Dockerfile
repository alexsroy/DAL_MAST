FROM ros:jazzy-ros-core

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
	build-essential \
	vim \
	nano \
	python3-colcon-common-extensions \
	python3-pygame \
	python3-serial \
	glpk-utils \
	libudev-dev \
	libfastcdr-dev \
	ros-jazzy-rmw-fastrtps-cpp \
	ros-jazzy-rosidl-typesupport-fastrtps-cpp \
	ros-jazzy-tf2-msgs \
	ros-jazzy-turtlesim \
	ros-jazzy-xacro \
	ros-jazzy-robot-state-publisher \
	ros-jazzy-nmea-msgs \
	ros-jazzy-mavros-msgs \
	&& rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

WORKDIR /workspace
CMD ["bash"]
