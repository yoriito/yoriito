---
chapter_no: 5
---

{{ sec_reset(chapter_no) }}

# Part2 Practice

## {{ h2_sec("Building Your First Yoriito Vehicle API Application 📱") }}

### {{ h3_sec("Introduction") }}

In this tutorial, you will learn how to use the Yoriito Signal API through sample code, and build a sample application with it.
By running the development environment you built in [Chapter 4](../04_environment_setup/04_environment_setup.md), you can experience application development using the Yoriito Signal API.

### {{ h3_sec("Basics") }}

The Yoriito Signal API is a set of APIs that correspond one-to-one with Yoriito VSS.  
It consists of:

1.  Get – to obtain the current value  
1.  Set – to set a target value  
1.  Subscribe – to continuously receive changes in the current value  

This section shows sample code for each of these.

![Yoriito_Tutorial_BasicDiagram](assets/Yoriito_Tutorial_BasicDiagram.svg)

For more details on the Yoriito Signal API, see ["2. System Configuration/Scope/Versioning"](../02_system_scope_versioning/02_system_scope_versioning.md). For more details on VSS, see ["3. VSS/VISS"](../03_VSS_VISS/03_vss_viss.md).

Try running and modifying the sample code, and apply it to your own application development. To check the behavior of the sample code, make sure to start the simulator first by following "4-6. Start the simulator".

#### {{ h4_sec("Check the current state of the high beam: Get") }}

**What is `Get`?**  

- `Get` is used when you want to obtain the current value.
- You can call `Get` for signals whose type is Actuator / Sensor / Attribute.

**Sample code** (`yoriito-tutorial/tutorial/get/src/main.cc`)

- The following code retrieves the current high-beam state (ON/OFF).

```cpp
#include "yoriito/yoriito_log.h"
#include <yoriito/signal/body/Body.h>

namespace {
constexpr int kExitOk = 0;
constexpr int kExitNg = 1;
} // namespace

int main() {
  YORIITO_LOG_INITIALIZE("get");

  auto result = yoriito::vehicle::body::lights::beam::high::ison::Get();

  if (result.IsErr()) {
    auto err = result.TakeErr();
    YORIITO_LOG_ERROR("get", std::string("Get failed: ") + err->Message() +
                                 " (code=" + std::to_string(err->ErrorCode()) +
                                 ")");
    YORIITO_LOG_FINALIZE();
    return kExitNg;
  }

  auto data_point = result.TakeOk().value();
  const bool value = data_point.GetData();

  YORIITO_LOG_INFO("get",
                   std::string("Get succeeded: ") + (value ? "true" : "false"));

  YORIITO_LOG_FINALIZE();
  return kExitOk;
}
```

**Build & run steps**  

1. Start the simulator if it is not running yet.

    ```shell
    $ cd /work/ref_pal
    $ npm ci
    $ ./init_pal.sh
    $ npx electron . --no-sandbox
    ```

1. Build

    ```shell
    $ cd /work/tutorial/get
    $ cmake -S . -B build
    $ cmake --build build -j
    ```

1. Run

    ```shell
    $ ./build/get
    ```

!!! info
    If the command fails with a `No data` error, rerun `./init_pal.sh` to initialize the signal data, then retry the command.

**Example use cases**  

- Display the current state on the screen
    - e.g., get "High beam: ON/OFF", "Wiper: AUTO" and reflect them in the UI
- Get the current value only when needed
    - e.g., fetch values only when the user presses a "Refresh" button

#### {{ h4_sec("Turn on the high beam: Set") }}

**What is `Set`?**  

- `Set` is used when you want to set a target value.
- You can call `Set` only for signals whose type is Actuator.

**Sample code** (`yoriito-tutorial/tutorial/set/src/main.cc`)

```cpp
#include "yoriito/yoriito_log.h"
#include <yoriito/signal/body/Body.h>

namespace {
constexpr int kExitOk = 0;
constexpr int kExitNg = 1;
} // namespace

int main() {
  YORIITO_LOG_INITIALIZE("set");

  const bool is_on = true;
  yoriito::Result<void> set_result =
      yoriito::vehicle::body::lights::beam::high::ison::Set(is_on);

  if (set_result.IsErr()) {
    const yoriito::Result<void>::ErrorPtr err = set_result.TakeErr();
    YORIITO_LOG_ERROR("set", std::string("Set failed: ") + err->Message() +
                                 " (code=" + std::to_string(err->ErrorCode()) +
                                 ")");
    YORIITO_LOG_FINALIZE();
    return kExitNg;
  }

  YORIITO_LOG_INFO(
      "set", std::string("Set succeeded: ") + (is_on ? "true" : "false"));

  YORIITO_LOG_FINALIZE();
  return kExitOk;
}
```

**Build & run steps**  

1. Start the simulator if it is not running yet.

    ```shell
    $ cd /work/ref_pal
    $ npm ci
    $ ./init_pal.sh
    $ npx electron . --no-sandbox
    ```

1. Build

    ```shell
    $ cd /work/tutorial/set
    $ cmake -S . -B build
    $ cmake --build build -j
    ```

1. Run

    ```shell
    $ ./build/set
    ```

!!! info
    If the command fails with a `No data` error, rerun `./init_pal.sh` to initialize the signal data, then retry the command.

**Example use cases**  

- Control vehicle functions based on user operations
    - e.g., high beam ON/OFF, A/C temperature setting, seat heater ON/OFF etc.

#### {{ h4_sec("Receive a high-beam state change: Subscribe") }}

**What is `Subscribe`?**  

- `Subscribe` is used when you want to continuously receive changes in the current value.
- You can call `Subscribe` for signals whose type is Actuator / Sensor.
- In this sample, the application waits for one high-beam state update, outputs the received value, and then calls `UnSubscribe` to end the subscription.

**Sample code** (`yoriito-tutorial/tutorial/subscribe/src/main.cc`)

```cpp
#include "yoriito/yoriito_log.h"
#include <yoriito/signal/body/Body.h>

namespace {
constexpr int kExitOk = 0;
constexpr int kExitNg = 1;

namespace high_beam = yoriito::vehicle::body::lights::beam::high::ison;
} // namespace

int main() {
  YORIITO_LOG_INITIALIZE("subscribe");

  auto subscribe_result = high_beam::Subscribe();
  if (subscribe_result.IsErr()) {
    auto error = subscribe_result.TakeErr();
    YORIITO_LOG_ERROR("subscribe",
                      std::string("Subscribe failed: ") + error->Message() +
                          " (code=" + std::to_string(error->ErrorCode()) + ")");
    YORIITO_LOG_FINALIZE();
    return kExitNg;
  }

  auto subscription_context = subscribe_result.TakeOk().value();
  YORIITO_LOG_INFO("subscribe", "Waiting for one update...");

  int exit_code = kExitOk;

  auto message_result = subscription_context.Messages();
  if (message_result.IsErr()) {
    auto error = message_result.TakeErr();
    YORIITO_LOG_ERROR("subscribe",
                      std::string("Messages() failed: ") + error->Message() +
                          " (code=" + std::to_string(error->ErrorCode()) + ")");
    exit_code = kExitNg;
  } else {
    auto data_point = message_result.TakeOk().value();
    const bool is_on = data_point.GetData();

    YORIITO_LOG_INFO("subscribe", std::string("IsOn updated: ") +
                                      (is_on ? "true" : "false"));
  }

  auto unsubscribe_result =
      high_beam::UnSubscribe(std::move(subscription_context));
  if (unsubscribe_result.IsErr()) {
    auto error = unsubscribe_result.TakeErr();
    YORIITO_LOG_ERROR("subscribe",
                      std::string("UnSubscribe failed: ") + error->Message() +
                          " (code=" + std::to_string(error->ErrorCode()) + ")");
    exit_code = kExitNg;
  } else {
    YORIITO_LOG_INFO("subscribe", "UnSubscribe succeeded.");
  }

  YORIITO_LOG_FINALIZE();
  return exit_code;
}
```

**Build & run steps**  

1. Start the simulator if it is not running yet.

    ```shell
    $ cd /work/ref_pal
    $ npm ci
    $ ./init_pal.sh
    $ npx electron . --no-sandbox
    ```

1. Build

    ```shell
    $ cd /work/tutorial/subscribe
    $ cmake -S . -B build
    $ cmake --build build -j
    # If not already done, build Set as well
    $ cd /work/tutorial/set
    $ cmake -S . -B build
    $ cmake --build build -j
    ```

1. Run
    - First, run `Subscribe`:

        ```shell
        $ cd /work/tutorial/subscribe
        $ ./build/subscribe 
        ```

    - Then, in another terminal, run `Set`:

        ```shell
        $ cd /work/tutorial/set
        $ ./build/set
        ```

    - After `Set` runs, the `Subscribe` process receives one update, unsubscribes, and exits.

!!! info
    If the command fails with a `No data` error, rerun `./init_pal.sh` to initialize the signal data, then retry the command.

**Example use cases**

- Reflect state changes in the UI in real time
    - e.g., when the physical high-beam switch changes ON/OFF, the app UI updates immediately
- Detect abnormalities
    - e.g., show a warning if temperature exceeds a specified value


### {{ h3_sec("Advanced") }}

In the Basics section, you learned how to obtain and control vehicle signals using `Get` / `Set` / `Subscribe` of the Yoriito Signal API. In the Advanced section, you will learn concepts needed to develop more realistic applications, along with sample code.

#### {{ h4_sec("Check whether the front fog light is available: Availability") }}

**What is `Availability`?**

- In the Basics section, sample code for `Get` / `Set` / `Subscribe` assumed that the high-beam signal is available.
- In this section, the sample code checks the availability of the front fog light as both a sensor and an actuator.
- In real vehicles, however, a signal may or may not be usable depending on the vehicle state and conditions. A function may be available on one vehicle but not on another.
- To inform applications of these differences, `Availability` is provided to represent whether a signal is usable.
- Availability takes either `true` or `false`:
    - `true`: the signal is currently available  
    - `false`: the signal exists but is currently unavailable
- Depending on the kind of signal, two types of Availability are defined:
    - `Availability_Sensor`  
        - Indicates whether the current value can be obtained via `Get`.
    - `Availability_Actuator`  
        - Indicates whether the target value can be set via `Set`.
- For more details on Availability, see ["2-5. System Behavior"](../02_system_scope_versioning/02_system_scope_versioning.md#2-5-system-behavior).

**Sample code** (`yoriito-tutorial/tutorial/availability/src/main.cc`)

```cpp
#include "yoriito/yoriito_log.h"
#include <yoriito/signal/body/Body.h>

namespace {
constexpr int kExitOk = 0;
constexpr int kExitNg = 1;
} // namespace

int main() {
  YORIITO_LOG_INITIALIZE("availability");
  auto result = yoriito::vehicle::body::lights::fog::front::ison::Get();

  if (result.IsErr()) {
    auto err = result.TakeErr();
    YORIITO_LOG_ERROR("availability",
                      std::string("Get failed: ") + err->Message() +
                          " (code=" + std::to_string(err->ErrorCode()) + ")");
    YORIITO_LOG_FINALIZE();
    return kExitNg;
  }

  auto data_point = result.TakeOk().value();
  const bool is_available_sensor = data_point.IsAvailableSensor();
  const bool is_available_actuator = data_point.IsAvailableActuator();

  YORIITO_LOG_INFO("availability",
                   std::string("Available Sensor: ") +
                       (is_available_sensor ? "true" : "false"));
  YORIITO_LOG_INFO("availability",
                   std::string("Available Actuator: ") +
                       (is_available_actuator ? "true" : "false"));

  YORIITO_LOG_FINALIZE();
  return kExitOk;
}
```

**Build & run steps**  

1. Start the simulator if it is not running yet.

    ```shell
    $ cd /work/ref_pal
    $ npm ci
    $ ./init_pal.sh
    $ npx electron . --no-sandbox
    ```

1. Build

    ```shell
    $ cd /work/tutorial/availability
    $ cmake -S . -B build
    $ cmake --build build -j
    ```

1. Run

    ```shell
    $ ./build/availability
    ```

!!! tip
    Try changing the signal in the sample code to another one, then rebuild and run. For example, if you change it to `yoriito::vehicle::body::lights::beam::high::ison`, both sensor and actuator availability should be `true`.


**Example use cases**

Availability is mainly used in the following situations:

- GUI control
    - Automatically gray out buttons for unavailable functions.
- User guidance
    - Show messages such as "Currently not operable" when conditions are not met (e.g., while driving).
- Check before sending operation requests
    - Verify availability before sending an operation request via the API.

This ensures the UI/application behavior stays consistent with the actual vehicle state.

#### {{ h4_sec("Get detailed information (metadata) of the high beam: Inspect") }}

**What is `Inspect`?**

- In the Basics section, we dealt with Boolean signals. In real vehicles, there are also `int` and `float` signals.
- In such cases, you may want to know the minimum and maximum values.
- For example, for vehicle speed, you may want to know whether the unit is km/h or mph.
- For this purpose, the `Inspect` method is provided.
- By calling `Inspect`, you can get detailed information (metadata) of a signal.
- Key data fields obtainable via `Inspect`:

    | Data            | Meaning                                                             |
    | --------------- | ------------------------------------------------------------------- |
    | `path`          | Full path of the signal (e.g. `Vehicle.Body.Lights.Beam.High.IsOn`) |
    | `datatype`      | Data type (e.g. `boolean`, `int`, `float`, `string`)                |
    | `entry_type`    | Node type: `branch` / `sensor` / `actuator` / `attribute`           |
    | `unit`          | Unit (e.g. `km/h`, `%`, `°C`)                                       |
    | `min`           | Minimum value                                                       |
    | `max`           | Maximum value                                                       |
    | `comment`       | Additional notes                                                    |
    | `allowed`       | Allowed values (e.g. `['AUTO', 'LOW', 'MID', 'HIGH']`)              |
    | `default_value` | Default value                                                       |
    | `description`   | Description of the signal                                           |
    | `array_size`    | Number of elements if it is an array                                |


**Sample code** (`yoriito-tutorial/tutorial/inspect/src/main.cc`)

```cpp
#include "yoriito/yoriito_log.h"
#include <yoriito/signal/body/Body.h>

namespace {
constexpr int kExitOk = 0;
constexpr int kExitNg = 1;
} // namespace

int main() {
  YORIITO_LOG_INITIALIZE("inspect");

  auto result = yoriito::vehicle::body::lights::beam::high::ison::Inspect();

  if (result.IsErr()) {
    auto err = result.TakeErr();
    YORIITO_LOG_ERROR("inspect",
                      std::string("Inspect failed: ") + err->Message() +
                          " (code=" + std::to_string(err->ErrorCode()) + ")");
    YORIITO_LOG_FINALIZE();
    return kExitNg;
  }

  auto inspect_response = result.TakeOk().value();
  auto data_points = inspect_response.GetDataPoints();

  if (data_points.empty()) {
    YORIITO_LOG_ERROR("inspect", "Inspect failed: No data points returned.");
    YORIITO_LOG_FINALIZE();
    return kExitNg;
  }

  const auto &inspect_data = data_points.front();

  const auto &path = inspect_data.GetPath();
  // const auto &data_type = inspect_data.GetDataType();
  // const auto &entry_type = inspect_data.GetEntryType();
  // const auto &deprecation = inspect_data.GetDeprecation();
  // const auto &unit = inspect_data.GetUnit();
  // const auto &min = inspect_data.GetMin();
  // const auto &max = inspect_data.GetMax();
  // const auto &comment = inspect_data.GetComment();
  // const auto &allowed = inspect_data.GetAllowed();
  // const auto &default_value = inspect_data.GetDefaultValue();
  const auto &description = inspect_data.GetDescription();
  // const auto &array_size = inspect_data.GetArraySize();
  // const auto &pattern = inspect_data.GetPattern();
  // const auto &custom_attributes = inspect_data.GetCustomAttributes();

  YORIITO_LOG_INFO("inspect", "Inspect succeeded");
  YORIITO_LOG_INFO("inspect", std::string("Path: ") + path);
  YORIITO_LOG_INFO("inspect", std::string("Description: ") + description);

  YORIITO_LOG_FINALIZE();
  return kExitOk;
}
```

**Build & run steps**  

1. Start the simulator if it is not running yet.

    ```shell
    $ cd /work/ref_pal
    $ npm ci
    $ ./init_pal.sh
    $ npx electron . --no-sandbox
    ```

1. Build

    ```shell
    $ cd /work/tutorial/inspect
    $ cmake -S . -B build
    $ cmake --build build -j
    ```

1. Run

    ```shell
    $ ./build/inspect 
    ```

**Example use cases**

Inspect is mainly used in the following situations:

- Check before sending operation requests
    - Confirm that the value to be set is within the min/max range of the signal.
- GUI control
    - Display min/max values for temperature settings or window opening percentage.
    - Prevent users from setting values outside the valid range.
- Support multiple vehicle types
    - Obtain the correct range even when controllable ranges differ across vehicle types and equipment.

#### {{ h4_sec("Control the simulator vehicle via Text User Interface (TUI)") }}

So far, you have learned the Yoriito Signal API through coding. VSS defines many more signals, and various applications can be developed using them.

Writing code each time just to check a signal's behavior is time-consuming.
For this purpose, a Text User Interface is provided. For usage, see "Connect vshot" in [the PAL developer tutorial](../07_develop_pal/07_develop_pal.md).


### {{ h3_sec("Troubleshooting") }}

#### {{ h4_sec('"Tools or libraries not found" errors') }}

- Cause  
    You may be running commands in the host environment instead of inside the container.

- Countermeasure  
    - Start the container as described in ["4-5. Start the container"](../04_environment_setup/04_environment_setup.md) and run commands in a terminal inside the container.
    - All required tools and libraries are already installed in the container.
    

#### {{ h4_sec('"Cannot connect to `localhost (127.0.0.1)`" error') }}

- Cause  
    Even local communication (`localhost` / `127.0.0.1`) may be routed through a proxy, which can prevent a proper connection to `localhost`.
    
- Countermeasure  
    - Check the proxy-related environment variables (`no_proxy` / `NO_PROXY`) in the container.  
    - Running the following commands in the container terminal may resolve the issue:

        ```shell
        $ export no_proxy=127.0.0.1,localhost  
        $ export NO_PROXY=127.0.0.1,localhost  
        ```

    - If this resolves the issue, add `remoteEnv` to `.devcontainer/devcontainer.json` so that the setting persists after restarting the container. After changing the settings, rebuild the Dev Container.

        ```json
        "remoteEnv": {
          "no_proxy": "127.0.0.1,localhost",
          "NO_PROXY": "127.0.0.1,localhost"
        },
        ```
