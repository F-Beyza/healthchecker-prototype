# HealthChecker Prototype

This repository contains a prototype Python application designed to fetch, process,
and visualize telemetry data from multiple sensors.

## Features
- Token-based API interaction (mocked)
- Date to timestamp conversion
- Multiple device (MAC-based) telemetry handling
- Modular and class-based design

## Project Structure


flowchart LR
 subgraph SensorProcessor["SensorProcessor"]
        A1["fetch_token"]
        A2["date_to_timestamp"]
        A3["fetch_device_id"]
        A4["fetch_all_telemetry"]
        A5["process_sensors_visualize"]
        A6["visualize_telemetry"]
  end
    User["User"] --> SensorProcessor
    SensorProcessor --> Logger["Logger"] & Matplotlib["Matplotlib"]
    fetch_all_telemetry["fetch_all_telemetry"] --> MockAPI[("Mock Raw Data")]