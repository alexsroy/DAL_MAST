# DAL MAST ROS2 Project

This is the official source code repository for the Dalhousie University Marine Autonomous Sailboat Team.

> [!NOTE]
> The code is still under construction, many features are incomplete or actively under development.

# Development

### Dependencies

To aid in the development of the project, ensure you have Docker version `29.1.5` or similar installed locally. If you don't have Docker, you can download it [here](https://www.docker.com/get-started/) for your specific architecture or computer configuration. We use Docker to containerise the ROS2 project and ensure the dependencies are consistent and accessible across machines. 

Also ensure that you have bash installed, as we assume that it is your current active shell for scripts and cli commands. 

> [!TIP]
> Once you have Docker installed, you can verify its installation by entering `docker -v` into your terminal. You should get an output like this: `Docker version 29.1.5, build v29.1.5`.

### Contributions

Next, clone the repository to your local machine and enter the root directory within the project:

```bash
# enter these commands in your terminal

git clone https://github.com/alexsroy/DAL_MAST
cd DAL_MAST
```

> [!IMPORTANT]
> Before we continue, it is important to ensure that you are either on the develop branch or a custom-made branch when developing this project. Do not push code to the main branch directly. To check your branch, you can use `git branch`, and to switch branches use `git switch develop` to switch to the develop branch.

Editing code can be done in your text editor of choice. It is necessary to have an instance of the project environment running on the Docker container while developing to run and test your code.

To enter the container, simply run the startup script in the root project directory with `./startup.sh`. This will build and step you into the container. Once you are in the container, you are able to execute the run command documented below to launch your code.

> [!NOTE]
> If it is your first time building the project, it may take a few minutes to build the container.

### Running and Launching Modules

Since our code is in active development, we don't have a clean way yet of launching the ROS2 modules. To start each script at the moment, you can run the following command from the project's root directory:

```bash
# the module names are documented below

ros2 run py_tut module-name-here
```

The accessible module names currently are as follows:
- navi
- boat
- ctrl
- comm
- wayp

> [!TIP]
> To easily launch all of the modules at the same time, navigate to the root of the project and run the `launch.sh` file.
