---
chapter_no: 4
---

{{ sec_reset(chapter_no) }}

# Part2 Practice  

## {{ h2_sec("Setting Up the Application Development Environment 📱🚗") }}

### {{ h3_sec("Introduction") }}

In this chapter, we will set up the development environment required to smoothly follow the tutorial.

The overall structure of the tutorial environment is shown in the diagram below. 

In this tutorial, you will launch a development container on Ubuntu running on Windows Subsystem for Linux 2 (WSL2), then connect to the container from VS Code via the Dev Containers extension. From there, you will perform coding, building, and running the application.

![yoriito_tutorial_env](assets/yoriito_tutorial_env.svg)

!!! info  
    Depending on your network environment, some download/installation steps may fail. If the process does not proceed or times out partway through, please check your network settings.


### {{ h3_sec("Recommended Environment") }}

The recommended operating environment is as follows:  

- OS: Windows 11  
- Virtualization: WSL2  
- Linux distribution: Ubuntu 24.04 LTS (on WSL2)


### {{ h3_sec("Prerequisites") }}

1. Please install the following on Windows 11.  
    - VS Code  
        - <https://code.visualstudio.com/>

1. Please install the following on Ubuntu.
    - Git  
    - Docker  

1. Please install the following extension in VS Code.
    - Dev Containers  
        - <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers>


### {{ h3_sec("Clone the Repository") }}

1. Open an Ubuntu terminal.

1. Clone the sample application repository.  

    ```shell
    $ git clone https://github.com/yoriito/yoriito-tutorial.git
    ```

1. Fetch submodules.  

    ```shell
    $ cd yoriito-tutorial
    $ git submodule update --init --recursive
    ```


### {{ h3_sec("Start the Container") }}

Yoriito repositories typically support dev containers. In this section, you will set up the environment using a dev container.

1. In the target repository's root directory, start VS Code:  

    ```shell
    $ code .
    ```

1. After VS Code starts, open the Command Palette with `Ctrl` + `Shift` + `P`.

1. Type `Dev Containers: Rebuild` and select "Dev Containers: Rebuild and Reopen in Container".

1. The container will be built and various libraries will be installed.

1. After VS Code reopens in the development container, open a terminal inside the container. Run all commands in this chapter and subsequent chapters from this terminal.

!!! info
    A video is also available as a reference.

    <video controls width="800">
      <source src="../assets/build_devcontainer.mp4" type="video/mp4">
    </video>


### {{ h3_sec("Start the Simulator") }}

This section explains how to start the simulator used to reproduce actual vehicle behavior throughout the tutorial.

1. Move to the ref_pal directory.  

    ```shell
    $ cd /work/ref_pal
    ```

1. Run the following commands.  

    ```shell
    $ npm ci
    $ ./init_pal.sh
    $ npx electron . --no-sandbox
    ```
