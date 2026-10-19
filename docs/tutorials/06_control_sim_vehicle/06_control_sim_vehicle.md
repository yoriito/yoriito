---
chapter_no: 6
---

{{ sec_reset(chapter_no) }}

# Part2 Practice

## {{ h2_sec("Controlling the Simulator Vehicle 📱") }}

### {{ h3_sec("Introduction") }}

In the previous chapter, we looked at sample code that demonstrates how to use the Yoriito Signal API. In this chapter, we introduce a sample application that makes practical use of the Yoriito Signal API.


### {{ h3_sec("Understand the App Architecture") }}

The overall architecture of the sample application is shown in the figure below.

![Yoriito_RefAppComponentDiagram](assets/Yoriito_RefAppComponentDiagram.svg)

**<u>GUI Application (Flutter)</u>**  

- This is the front‑end (screen) operated by the user, implemented with Flutter.  
- In this sample, the GUI Application and the Headless Application are separated into different processes so that the UI framework can be replaced more easily.  
- However, when using the API, neither Flutter nor this process separation is mandatory.  
- This architecture is presented simply as one example of how to develop a GUI Application using the Yoriito Signal API.  
- Target code: `yoriito-tutorial/ref_ui`

**<u>Headless Application (C++)</u>**  

- This is the back-end (non-GUI) application that acts as a BFF (Backend For Frontend), processing requests from the GUI Application.  
- It calls the Yoriito Signal API and communicates with the GUI Application via gRPC.  
- It is implemented in C++.  
- Target code: `yoriito-tutorial/ref_app`

**<u>Yoriito Signal API</u>**  

- This is the vehicle‑oriented API used from the Headless Application.  
- The API is provided as shared libraries named `libyoriito_vehicle_api_<domain>.so`.

**<u>Yoriito VISS Server</u>**  

- As a data broker, it relays vehicle signal information from PAL to applications, and forwards actuator control requests from applications to PAL.

**<u>PAL</u>**  

- This is the lowest layer, directly interfacing with the platform-dependent I/O and the physical vehicle.  
- In this tutorial, the 3D car model plays this role.  
- Target code: `yoriito-tutorial/ref_pal`


### {{ h3_sec("Understand the App Contents") }}

The sample application features an emergency button. When you press the emergency button in the app, windows and doors close, and lights turn on.

![emergency_app_v1-20260129-092341](assets/emergency_app_v1-20260129-092341.gif)



### {{ h3_sec("Verify the App Behavior") }}

Run all commands in this section in terminals inside the development container configured in ["4. Setting Up the Application Development Environment"](../04_environment_setup/04_environment_setup.md).

1. Start the simulator (PAL)  

    1. Move to the `ref_pal` directory.
        ```shell
        $ cd /work/ref_pal
        ``` 

    1. Run the following commands.
        ```shell
        $ npm ci
        $ ./init_pal.sh
        $ npx electron . --no-sandbox
        ```

1. Start the Headless Application  

    1. Move to the `ref_app` directory.
        ```shell
        $ cd /work/ref_app
        ```

    1. Build the application.
        ```shell
        $ cmake -S . -B build 
        $ cmake --build build
        ```

    1. Run the application.
        ```shell
        $ ./build/ref_app
        ```

1. Start the GUI Application  

    1. Move to the `ref_ui` directory.
        ```shell
        $ cd /work/ref_ui
        ```

    1. Build and run.
        ```shell
        $ flutter clean
        $ flutter pub get
        $ flutter run -d linux
        ```

### {{ h3_sec("Troubleshooting") }}

#### {{ h4_sec('"Address already in use" error appears at startup') }}

- Cause  
    - The gRPC port numbers used by the Yoriito VISS Server or the Headless Application may conflict with those of other applications.  
    - This is likely to occur if multiple samples or stale processes are still running in the same environment.

- Countermeasure  
    - Check which port numbers are used in this tutorial and make sure there are no other processes using the same ports.

        | **Port** | **Component**                  |
        | -------- | ------------------------------ |
        | 50052    | Yoriito VISS Server (consumer) |
        | 50053    | Yoriito VISS Server (producer) |
        | 50055    | Headless Application           |
