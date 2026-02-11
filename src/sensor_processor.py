import matplotlib.pyplot as plt
from datetime import datetime
from logger_config import setup_logger
import secrets
import string

logger = setup_logger(__name__)

class SensorProcessor:

    def __init__(self, url):
        self.url = url

    def fetch_token(self):
        alphabet = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(alphabet) for _ in range(32))

        logger.info(f"[fetch_token] Generated token for {self.url}")
        logger.debug(f"Token value: {token}")
        return token

    def date_to_timestamp(self, date_str):
        logger.info(f"[date_to_timestamp] Converting date to timestamp: {date_str}")
        return 123456789

    def fetch_device_id(self, mac_id):
        logger.info(f"[fetch_device_id] Fetching device ID for MAC: {mac_id}")
        return "dummy_device_id"

    def fetch_all_telemetry(self, mac_id, device_id, start_ts, end_ts):
        logger.info(f"Fetching all telemetry for MAC: {mac_id}, Device: {device_id}")
        logger.info(f"Start Timestamp: {start_ts}, End Timestamp: {end_ts}")

        return {
            "temperature": [
                {"ts": 1710000000000, "value": 25},
                {"ts": 1710000100000, "value": 26}
            ]
        }

    def fetch_telemetry(self, mac_id, keyword, start_ts, end_ts):
        device_id = self.fetch_device_id(mac_id)
        raw_data = self.fetch_all_telemetry(mac_id, device_id, start_ts, end_ts)

        if not isinstance(raw_data, dict):
            return []

        formatted_list = []

        for entry in raw_data.get(keyword, []):
            formatted = {
                "ts": entry.get("ts"),
                "value": entry.get("value")
            }
            formatted_list.append(formatted)

        return formatted_list

    # GRAPH EXPORT
    def visualize_telemetry(self, title, data):

        if not data:
            logger.warning("No telemetry data to visualize")
            return

        timestamps = []
        values = []

        for entry in data:
            ts = entry["ts"] / 1000  # convert ms to seconds
            dt = datetime.fromtimestamp(ts)
            timestamps.append(dt)
            values.append(entry["value"])

        plt.figure()
        plt.plot(timestamps, values)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.xticks(rotation=45)
        plt.tight_layout()

        filename = "telemetry_output.png"
        plt.savefig(filename)
        plt.close()

        logger.info(f"Telemetry visualization saved as {filename}")

    def process_sensors_visualize(self, keyword, start_date, end_date, title, mac_list):

        token = self.fetch_token()

        start_ts = self.date_to_timestamp(start_date)
        end_ts = self.date_to_timestamp(end_date)

        all_results = []

        for mac_id in mac_list:
            telemetry_data = self.fetch_telemetry(mac_id, keyword, start_ts, end_ts)
            all_results.extend(telemetry_data)

        self.visualize_telemetry(title, all_results)


processor = SensorProcessor(url="https://api.test.com")

if __name__ == "__main__":
    processor.process_sensors_visualize(
        keyword="temperature",
        start_date="2024-01-01",
        end_date="2024-01-02",
        title="Sensor Data",
        mac_list=["AA:BB:CC", "11:22:33"]
    )
