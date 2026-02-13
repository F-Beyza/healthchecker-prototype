# HealthChecker Prototype

This repository contains a prototype Python application designed to fetch, process,
and visualize telemetry data from multiple sensors.

## Features
- Token-based API interaction (mocked)
- Date to timestamp conversion
- Multiple device (MAC-based) telemetry handling
- Modular and class-based design

## Project Structure


## 🔁 Process Flow



```mermaid
flowchart TD
    A[Program Start] --> B[Get script directory]
    B --> C[Build CSV file path]
    C --> D[Create SensorProcessor instance]

    D --> E[Call process_sensors_visualize]

    E --> F[Convert start_date to timestamp]
    E --> G[Convert end_date to timestamp]

    F --> H{Are timestamps valid?}
    G --> H

    H -- No --> Z1[Exit process]
    H -- Yes --> I[Call fetch_telemetry]

    I --> J{Does CSV file exist?}
    J -- No --> Z2[Return None and empty list]
    J -- Yes --> K[Open CSV file]

    K --> L[Iterate through rows]
    L --> M{Row valid format?}
    M -- No --> L
    M -- Yes --> N{Sensor type matches keyword?}
    N -- No --> L
    N -- Yes --> O[Parse timestamp and value]

    O --> P{Within date range?}
    P -- No --> L
    P -- Yes --> Q[Append to formatted_list]

    Q --> L
    L --> R[Sort formatted_list]

    R --> S[Return mac_id and telemetry_data]

    S --> T{Is telemetry_data empty?}
    T -- Yes --> Z3[Skip visualization]
    T -- No --> U[Build final title with MAC]

    U --> V[Call visualize_telemetry]

    V --> W{Is data empty?}
    W -- Yes --> Z4[Exit visualize]
    W -- No --> X[Convert timestamps to datetime]

    X --> Y[Plot graph using matplotlib]
    Y --> AA[Create graphs folder if needed]
    AA --> AB[Generate filename]
    AB --> AC[Save PNG file]
    AC --> AD[Close plot]

    AD --> AE[Process End]

```
