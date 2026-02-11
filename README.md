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
    A[Start Application] --> B[process_sensors_visualize()]
    B --> C[fetch_token()]
    C --> D[date_to_timestamp(start_date)]
    D --> E[date_to_timestamp(end_date)]
    E --> F{Loop MAC List}
    F -->|For each MAC| G[fetch_device_id(mac)]
    G --> H[fetch_all_telemetry()]
    H --> I{Raw Data Valid?}
    I -->|Yes| J[Filter by keyword]
    J --> K[Format Data]
    K --> L[Append to all_results]
    L --> F
    I -->|No| F
    F --> M[visualize_telemetry()]
    M --> N[Export telemetry_output.png]
```
