import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import csv
import logging
import os
import sys

# --- Logger Configuration ---
# Configures the logging to output to the console (stdout)
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

class SensorProcessor:

    def __init__(self, data_file):
        self.data_file = data_file
        logger.info(f"[__init__] SensorProcessor initialized. Target File: {self.data_file}")

    def date_to_timestamp(self, date_str):
        # Tries to parse different date formats
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                dt_obj = datetime.strptime(date_str, fmt)
                return dt_obj.timestamp() * 1000  # Convert to milliseconds
            except ValueError:
                continue
        logger.error(f"Date format not understood: {date_str}")
        return None

    def fetch_telemetry(self, keyword, start_ts, end_ts):
        logger.info(f"[>> ENTER fetch_telemetry] Searching for '{keyword}'...")

        if not os.path.exists(self.data_file):
            logger.error(f"[!! ERROR] File not found: {self.data_file}")
            return []

        formatted_list = []
        
        # Statistics counters
        stats = {
            "total_rows": 0, 
            "skipped_header": 0, 
            "wrong_keyword": 0, 
            "out_of_date": 0, 
            "valid": 0, 
            "errors": 0
        }

        with open(self.data_file, 'r') as f:
            reader = csv.reader(f)
            
            try:
                header = next(reader) # Skip header row
                stats["skipped_header"] = 1
            except StopIteration:
                return []

            for row in reader:
                stats["total_rows"] += 1
                
                # Check for incomplete rows
                if len(row) < 4: 
                    stats["errors"] += 1
                    continue 
                
                # Parse row data
                row_type = row[1].strip() 
                row_time = row[2].strip()  
                row_val  = row[3].strip() 

                # Filter by Keyword
                if row_type != keyword: 
                    stats["wrong_keyword"] += 1
                    continue

                try:
                    # Parse time and convert to timestamp
                    dt_obj = datetime.fromisoformat(row_time)
                    row_ts = dt_obj.timestamp() * 1000 
                    value = float(row_val)
                    
                    # Filter by Date Range
                    if start_ts <= row_ts <= end_ts:
                        formatted_list.append({"ts": row_ts, "value": value})
                        stats["valid"] += 1
                    else:
                        stats["out_of_date"] += 1
                        
                except (ValueError, TypeError):
                    stats["errors"] += 1
                    continue

        # Sort data by timestamp
        formatted_list.sort(key=lambda x: x['ts'])

        # Log the summary statistics
        logger.info(f"   [Summary] Total Rows Scanned: {stats['total_rows']}")
        logger.info(f"   [Summary] VALID DATA KEPT: {stats['valid']}")
        
        return formatted_list

    def visualize_telemetry(self, title, data):
        logger.info(f"[>> ENTER visualize_telemetry] Plotting graph: '{title}' ({len(data)} data points)")

        if not data:
            logger.warning("   [!! WARNING] No data provided to plot.")
            return

        timestamps = []
        values = []

        for entry in data:
            ts = entry["ts"] / 1000  # Convert back to seconds for plotting
            dt = datetime.fromtimestamp(ts)
            timestamps.append(dt)
            values.append(entry["value"])

        # Create the Plot
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, values, marker='o', linestyle='-', color='blue', label=title)
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("%CO2")
        plt.legend()
        plt.grid(True)
        
        # Format X Axis (Hours:Minutes)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.xticks(rotation=45)
        plt.tight_layout()

        # --- SAVE LOGIC ---
        # 1. Define the 'graphs' folder path relative to this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        graph_folder = os.path.join(script_dir, "graphs")

        # 2. Create the folder if it doesn't exist
        if not os.path.exists(graph_folder):
            os.makedirs(graph_folder)
            logger.info(f"   [Info] Created new directory: {graph_folder}")

        # 3. Generate a unique filename with timestamp
        current_time_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_title = title.replace(" ", "_")
        filename = f"{safe_title}_{current_time_str}.png"

        # 4. Save the figure
        output_path = os.path.join(graph_folder, filename)
        plt.savefig(output_path)
        plt.close()

        logger.info(f"   [EXIT] Graph saved to -> {output_path}")
        logger.info(f"[<< EXIT visualize_telemetry] Task complete.")

    def process_sensors_visualize(self, keyword, start_date, end_date, title):
        logger.info("="*60)
        logger.info(f"[>> PROCESS START] Params: {keyword} | {start_date} -> {end_date}")

        start_ts = self.date_to_timestamp(start_date)
        end_ts = self.date_to_timestamp(end_date)

        if start_ts is None or end_ts is None:
            logger.error("Invalid date format. Process aborted.")
            return
        
        telemetry_data = self.fetch_telemetry(keyword, start_ts, end_ts)
        self.visualize_telemetry(title, telemetry_data)
        logger.info("="*60)

# --- EXECUTION BLOCK ---
if __name__ == "__main__":
    print("\n--- PROGRAM START ---\n")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "sensor_data.csv")
    
    processor = SensorProcessor(data_file=csv_path)

    processor.process_sensors_visualize(
        keyword="co2",
        start_date="2026-01-30",   
        end_date="2026-01-31",     
        title="CO2 Sensor Data"
    )
    print("\n--- PROGRAM END ---\n")