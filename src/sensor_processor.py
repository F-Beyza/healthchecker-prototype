# # # import csv
# # # import matplotlib.pyplot as plt
# # # from datetime import datetime
# # # from logger_config import setup_logger
# # # import secrets
# # # import string
# # # import logging
# # # import os

# # # #logger = setup_logger(__name__)
# # # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# # # logger = logging.getLogger(__name__)

# # # class SensorProcessor:

# # #     # def __init__(self, url):
# # #     #     self.url = url
# # #     def __init__(self, data_file):
# # #         self.data_file = data_file

# # #     # def fetch_token(self):
# # #     #     alphabet = string.ascii_letters + string.digits
# # #     #     token = ''.join(secrets.choice(alphabet) for _ in range(32))

# # #         # logger.info(f"[fetch_token] Generated token for {self.data_file}")
# # #         # logger.debug(f"Token value: {token}")
# # #         # return token

# # #     # def date_to_timestamp(self, date_str):
# # #     #     logger.info(f"[date_to_timestamp] Converting date to timestamp: {date_str}")
# # #     #     return 123456789
# # #     def date_to_timestamp(self, date_str):
# # #         try:
# # #             dt_obj = datetime.strptime(date_str, "%Y-%m-%d")
# # #             return dt_obj.timestamp()
# # #         except ValueError:
# # #             logger.error(f"[date_to_timestamp] Invalid date format: {date_str}")
# # #             return None
# # #         # ts = dt_obj.timestamp() * 1000 # Milisaniyeye çevir
# # #         # logger.info(f"[date_to_timestamp] {date_str} -> {ts}")
# # #         # return ts

# # #     # def fetch_device_id(self, mac_id):
# # #     #     logger.info(f"[fetch_device_id] Fetching device ID for MAC: {mac_id}")
# # #     #     return "dummy_device_id"

# # #     # def fetch_all_telemetry(self, mac_id, device_id, start_ts, end_ts):
# # #     #     logger.info(f"Fetching all telemetry for MAC: {mac_id}, Device: {device_id}")
# # #     #     logger.info(f"Start Timestamp: {start_ts}, End Timestamp: {end_ts}")

# # #     #     return {
# # #     #         "temperature": [
# # #     #             {"ts": 1710000000000, "value": 25},
# # #     #             {"ts": 1710000100000, "value": 26}
# # #     #         ]
# # #     #     }
# # #     # def fetch_all_telemetry(self):
# # #     #     # Verileri JSON dosyasından okuyoruz
# # #     #     if not os.path.exists(self.data_file):
# # #     #         logger.error(f"Dosya bulunamadı: {self.data_file}")
# # #     #         return {}
# # #     #     with open(self.data_file, "r") as f:
# # #     #         data = json.load(f)
# # #     #     logger.info(f"Veriler {self.data_file} ok")
# # #     #     return data

# # #     # def fetch_telemetry(self, mac_id, keyword, start_ts, end_ts):
# # #     #     device_id = self.fetch_device_id(mac_id)
# # #     #     raw_data = self.fetch_all_telemetry(mac_id, device_id, start_ts, end_ts)

# # #     #     if not isinstance(raw_data, dict):
# # #     #         return []

# # #     #     formatted_list = []

# # #     #     for entry in raw_data.get(keyword, []):
# # #     #         formatted = {
# # #     #             "ts": entry.get("ts"),
# # #     #             "value": entry.get("value")
# # #     #         }
# # #     #         formatted_list.append(formatted)

# # #     #     return formatted_list
# # #     def fetch_telemetry(self, keyword, start_ts, end_ts):
# # #         if not os.path.exists(self.data_file):
# # #             logger.error(f"Data file not found: {self.data_file}")
# # #             logger.info("Returning empty telemetry data due to missing file.")
# # #             return []

# # #         # Dosyadan tüm veriyi çek
# # #         #raw_data = self.fetch_all_telemetry()
# # #         formatted_list = []

# # #         with open(self.data_file, 'r') as f:
# # #             reader = csv.reader(f)
# # #             next(reader, None)  
# # #             # Skip header row if there is one
# # #             for row in reader:
# # #                 # Assuming the CSV has headers: ts, value
# # #                 if len(row) < 4: continue # Skip if row doesn't have enough columns
# # #                 data_type = row[1].strip() # 'co2'
# # #                 time_str = row[2].strip()  # '2026-01-30 22:17:05...'
# # #                 value_str = row[3].strip()  # '25.0'

# # #                 if data_type != keyword: continue

# # #                 try:
# # #                     dt_obj = datetime.fromisoformat(time_str)
# # #                     ts = int(dt_obj.timestamp() * 1000)  # Convert to milliseconds
# # #                     value = float(value_str)
                    
# # #                     if start_ts <= ts <= end_ts:
# # #                         formatted_list.append({"ts": ts, "value": value})
# # #                 except (ValueError, TypeError) as e:
# # #                     logger.error(f"Error processing row {row}: {e}")
# # #                     continue

# # #         # data_list = raw_data
# # #         # formatted_list = []
# # #         # if not isinstance(raw_data, dict):
# # #         #     return []
# # #         formatted_list.sort(key=lambda x: x['ts'])
# # #         logger.info(f"Formatted telemetry data for '{keyword}': {formatted_list}")
# # #         return formatted_list
            
# # #         # Sadece tarih aralığına uyan verileri filtrele
# # #         # for entry in data_list.get(keyword, []):
# # #         #     ts = entry.get("ts")
# # #         #     if start_ts <= ts <= end_ts:  # Tarih filtresi
# # #         #         formatted = {
# # #         #             "ts": ts,
# # #         #             "value": entry.get("value")
# # #         #         }
# # #         #         formatted_list.append(formatted)


# # #         # logger.info(f"{len(formatted_list)} adet veri bulundu.")
# # #         # return formatted_list

# # #     # GRAPH EXPORT
# # #     def visualize_telemetry(self, title, data):

# # #         if not data:
# # #             logger.warning("No telemetry data to visualize")
# # #             return

# # #         timestamps = []
# # #         values = []

# # #         for entry in data:
# # #             ts = entry["ts"] / 1000  # convert ms to seconds
# # #             dt = datetime.fromtimestamp(ts)
# # #             timestamps.append(dt)
# # #             values.append(entry["value"])

# # #         plt.figure()
# # #         plt.plot(timestamps, values)
# # #         plt.title(title)
# # #         plt.xlabel("Time")
# # #         plt.ylabel("Value")
# # #         plt.xticks(rotation=45)
# # #         plt.tight_layout()

# # #         filename = "telemetry_output.png"
# # #         plt.savefig(filename)
# # #         plt.close()

# # #         logger.info(f"Telemetry visualization saved as {filename}")

# # #     def process_sensors_visualize(self, keyword, start_date, end_date, title):

# # #         #token = self.fetch_token()

# # #         start_ts = self.date_to_timestamp(start_date)
# # #         end_ts = self.date_to_timestamp(end_date)

# # #         # all_results = []

# # #         # for mac_id in mac_list:
# # #         if start_ts is None or end_ts is None:
# # #             logger.error("Tarih dönüşüm hatası nedeniyle işlem durduruldu.")
# # #             return
        
# # #         logger.info(f"Processing telemetry for keyword: {keyword}, Start: {start_date}, End: {end_date}")
# # #         telemetry_data = self.fetch_telemetry(keyword, start_ts, end_ts)
# # #         # all_results.extend(telemetry_data)
# # #         self.visualize_telemetry(title, telemetry_data)


# # # # processor = SensorProcessor(url="https://api.test.com")

# # # if __name__ == "__main__":

# # #     script_dir = os.path.dirname(os.path.abspath(__file__))
# # #     csv_path = os.path.join(script_dir, "sensor_data.csv")

# # #     processor = SensorProcessor(data_file=csv_path)

# # #     processor.process_sensors_visualize(
# # #         keyword="co2",
# # #         start_date="2026-01-30",
# # #         end_date="2026-01-31",
# # #         title="Sensor Data"
# # #         #mac_list=["AA:BB:CC", "11:22:33"]
# # #     )















# # # # import matplotlib.pyplot as plt
# # # # import matplotlib.dates as mdates
# # # # from datetime import datetime
# # # # import csv  # JSON yerine CSV kütüphanesi
# # # # import logging
# # # # import os

# # # # # --- Logger Ayarları ---
# # # # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# # # # logger = logging.getLogger(__name__)

# # # # class SensorProcessor:

# # # #     def __init__(self, data_file):
# # # #         self.data_file = data_file

# # # #     def date_to_timestamp(self, date_str):
# # # #         # Kullanıcının girdiği başlangıç/bitiş tarihini timestamp'e çevirir
# # # #         try:
# # # #             # Format: YIL-AY-GÜN SAAT:DAKİKA
# # # #             dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
# # # #             return dt_obj.timestamp()
# # # #         except ValueError:
# # # #             logger.error(f"Tarih formatı hatası! Beklenen: '2026-01-30 14:00'")
# # # #             return None

# # # #     def fetch_telemetry_csv(self, keyword, start_ts, end_ts):
# # # #         if not os.path.exists(self.data_file):
# # # #             logger.error(f"Dosya bulunamadı: {self.data_file}")
# # # #             return []

# # # #         formatted_list = []

# # # #         with open(self.data_file, 'r') as f:
# # # #             reader = csv.reader(f)
# # # #             # CSV Satırlarını okuyoruz: 
# # # #             # row[0] = ID, row[1] = Tür (co2), row[2] = Zaman, row[3] = Değer
# # # #             for row in reader:
# # # #                 if len(row) < 4: continue # Boş satır varsa atla

# # # #                 data_type = row[1].strip() # 'co2'
# # # #                 time_str = row[2].strip()  # '2026-01-30 22:17:05...'
# # # #                 value_str = row[3].strip() # '0.15'

# # # #                 # 1. Filtre: Sadece istediğimiz türü (örn: co2) alalım
# # # #                 if data_type != keyword:
# # # #                     continue

# # # #                 try:
# # # #                     # ISO formatındaki tarihi okuyoruz (fromisoformat Python 3.7+)
# # # #                     dt_obj = datetime.fromisoformat(time_str)
# # # #                     ts = dt_obj.timestamp() # Zaman damgasına çevir
                    
# # # #                     # Değeri sayıya çevir
# # # #                     value = float(value_str)

# # # #                     # 2. Filtre: Tarih aralığı kontrolü
# # # #                     if start_ts <= ts <= end_ts:
# # # #                         formatted_list.append({
# # # #                             "ts": ts,
# # # #                             "value": value
# # # #                         })

# # # #                 except ValueError as e:
# # # #                     logger.warning(f"Satır okuma hatası: {row} -> {e}")
# # # #                     continue

# # # #         formatted_list.sort(key=lambda x: x['ts']) # Tarihe göre sırala
# # # #         logger.info(f"{keyword} için {len(formatted_list)} veri bulundu.")
# # # #         return formatted_list

# # # #     def visualize_telemetry(self, title, data):
# # # #         if not data:
# # # #             logger.warning("Çizilecek veri yok!")
# # # #             return

# # # #         timestamps = []
# # # #         values = []

# # # #         for entry in data:
# # # #             dt = datetime.fromtimestamp(entry["ts"])
# # # #             timestamps.append(dt)
# # # #             values.append(entry["value"])

# # # #         # Grafik oluşturma
# # # #         fig, ax = plt.subplots(figsize=(10, 6))
# # # #         ax.plot(timestamps, values, marker='o', linestyle='-', color='red') # CO2 genelde kırmızı çizilir
        
# # # #         ax.set_title(title)
# # # #         ax.set_xlabel("Saat")
# # # #         ax.set_ylabel("Değer (CO2)")
# # # #         ax.grid(True)

# # # #         # X eksenini saat:dakika olarak formatla
# # # #         myFmt = mdates.DateFormatter('%H:%M')
# # # #         ax.xaxis.set_major_formatter(myFmt)
        
# # # #         plt.xticks(rotation=45)
# # # #         plt.tight_layout()

# # # #         filename = "telemetry_output.png"
# # # #         plt.savefig(filename)
# # # #         plt.close()
# # # #         logger.info(f"Grafik kaydedildi: {filename}")

# # # #     def process_sensors_visualize(self, keyword, start_date, end_date, title):
# # # #         start_ts = self.date_to_timestamp(start_date)
# # # #         end_ts = self.date_to_timestamp(end_date)

# # # #         if start_ts is None or end_ts is None:
# # # #             return

# # # #         logger.info(f"İşlem başlıyor: {start_date} -> {end_date} ({keyword})")
        
# # # #         # CSV'den verileri çek
# # # #         telemetry_data = self.fetch_telemetry_csv(keyword, start_ts, end_ts)
        
# # # #         # Görselleştir
# # # #         self.visualize_telemetry(title, telemetry_data)

# # # # # --- ÇALIŞTIRMA ---
# # # # if __name__ == "__main__":
# # # #     # CSV dosyasının adını buraya yazın
# # # #     script_dir = os.path.dirname(os.path.abspath(__file__))
# # # #     csv_path = os.path.join(script_dir, "sensor_data.csv")
# # # #     processor = SensorProcessor(data_file=csv_path)

# # # #     # keyword="co2" yaptık çünkü verinizde co2 yazıyor
# # # #     processor.process_sensors_visualize(
# # # #         keyword="co2",
# # # #         start_date="2026-01-30 21:00", 
# # # #         end_date="2026-01-30 23:00",
# # # #         title="CO2 Seviyesi"
# # # #     )
# # import matplotlib.pyplot as plt
# # import matplotlib.dates as mdates
# # from datetime import datetime
# # import csv
# # import logging
# # import os
# # import sys

# # # --- Logger Configuration ---
# # logging.basicConfig(
# #     level=logging.INFO, 
# #     format='%(asctime)s - %(levelname)s - %(message)s',
# #     handlers=[logging.StreamHandler(sys.stdout)]
# # )
# # logger = logging.getLogger(__name__)

# # class SensorProcessor:

# #     def __init__(self, data_file):
# #         self.data_file = data_file

# #     def date_to_timestamp(self, date_str):
# #         # Tries multiple formats: accepts both specific time and just the date
# #         for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
# #             try:
# #                 dt_obj = datetime.strptime(date_str, fmt)
# #                 # Convert to milliseconds to match the sensor data format
# #                 return dt_obj.timestamp() * 1000 
# #             except ValueError:
# #                 continue
        
# #         logger.error(f"Date format not understood: {date_str}")
# #         return None

# #     def fetch_telemetry(self, keyword, start_ts, end_ts):
# #         if not os.path.exists(self.data_file):
# #             logger.error(f"Data file not found: {self.data_file}")
# #             return []
# #         formatted_list = []
# #         with open(self.data_file, 'r') as f:
# #             reader = csv.reader(f)
            
# #             # Skip the header row (mac_id, sensor_label, etc.)
# #             try:
# #                 header = next(reader)
# #             except StopIteration:
# #                 return []

# #             for row in reader:
# #                 # Check if row is complete
# #                 if len(row) < 4: continue 
                
# #                 data_type = row[1].strip() 
# #                 time_str = row[2].strip()  
# #                 value_str = row[3].strip() 

# #                 if data_type != keyword: 
# #                     continue

# #                 try:
# #                     # Parse the ISO format date from the CSV
# #                     dt_obj = datetime.fromisoformat(time_str)
                    
# #                     # Convert to milliseconds
# #                     ts = dt_obj.timestamp() * 1000 
# #                     value = float(value_str)
                    
# #                     # Check if timestamp is within the requested range
# #                     if start_ts <= ts <= end_ts:
# #                         formatted_list.append({"ts": ts, "value": value})
                        
# #                 except (ValueError, TypeError) as e:
# #                     # logger.warning(f"Row error: {e}")
# #                     continue

# #         # Sort data by timestamp
# #         formatted_list.sort(key=lambda x: x['ts'])
# #         logger.info(f"Found {len(formatted_list)} records for '{keyword}'.")
# #         return formatted_list

# #     def visualize_telemetry(self, title, data):
# #         if not data:
# #             logger.warning("No data to visualize!")
# #             return

# #         timestamps = []
# #         values = []

# #         for entry in data:
# #             # Convert milliseconds back to seconds for plotting
# #             ts = entry["ts"] / 1000  
# #             dt = datetime.fromtimestamp(ts)
# #             timestamps.append(dt)
# #             values.append(entry["value"])

# #         plt.figure(figsize=(10, 6))
# #         plt.plot(timestamps, values, marker='o', linestyle='-', color='red')
# #         plt.title(title)
# #         plt.xlabel("Time")
# #         plt.ylabel("Value")
# #         plt.grid(True)
        
# #         # X-axis format (Hour:Minute)
# #         plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
# #         plt.xticks(rotation=45)
# #         plt.tight_layout()

# #         # 1. Get current time (YearMonthDay_HourMinuteSecond)
# #         current_time_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        
# #         # 2. Make the title safe for filenames (replace spaces with underscores)
# #         safe_title = title.replace(" ", "_")
        
# #         # 3. Combine them: "Title_Timestamp.png"
# #         filename = f"{safe_title}_{current_time_str}.png"

# #         # Save the image
# #         script_dir = os.path.dirname(os.path.abspath(__file__))
# #         output_path = os.path.join(script_dir, "telemetry_output.png")
# #         plt.savefig(output_path)
# #         plt.close()

# #         logger.info(f"GRAPH GENERATED: {output_path}")
# #         print(f"SUCCESS: New graph saved as -> {filename}")

# #     def process_sensors_visualize(self, keyword, start_date, end_date, title):
# #         start_ts = self.date_to_timestamp(start_date)
# #         end_ts = self.date_to_timestamp(end_date)

# #         if start_ts is None or end_ts is None:
# #             return
        
# #         logger.info(f"Process starting: {start_date} -> {end_date}")
# #         telemetry_data = self.fetch_telemetry(keyword, start_ts, end_ts)
# #         self.visualize_telemetry(title, telemetry_data)


# # if __name__ == "__main__":
# #     print("---SCRIPT STARTED---")

# #     script_dir = os.path.dirname(os.path.abspath(__file__))
# #     csv_path = os.path.join(script_dir, "sensor_data.csv")

# #     processor = SensorProcessor(data_file=csv_path)

# #     # Since your data is on Jan 30th, we select the range covering that day
# #     processor.process_sensors_visualize(
# #         keyword="co2",
# #         start_date="2026-01-30",   # Defaults to 00:00:00 if no time provided
# #         end_date="2026-01-31",     # Defaults to 00:00:00 if no time provided
# #         title="CO2 Sensor Data"
# #     )
# #     print("---SCRIPT ENDED---")

# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from datetime import datetime
# import csv
# import logging
# import os
# import sys

# # --- Logger Configuration ---
# # Logs will look like a trace: Time - Level - Message
# logging.basicConfig(
#     level=logging.INFO, 
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[logging.StreamHandler(sys.stdout)]
# )
# logger = logging.getLogger(__name__)

# class SensorProcessor:

#     def __init__(self, data_file):
#         self.data_file = data_file
#         logger.info(f"[__init__] SensorProcessor initialized. Target File: {self.data_file}")

#     def date_to_timestamp(self, date_str):
#         logger.info(f"   [>> ENTER date_to_timestamp] Input: '{date_str}'")
        
#         # Try multiple formats
#         for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
#             try:
#                 dt_obj = datetime.strptime(date_str, fmt)
#                 ts_ms = dt_obj.timestamp() * 1000
#                 logger.info(f"   [<< EXIT date_to_timestamp] Success. Converted '{date_str}' -> {ts_ms} (ms)")
#                 return ts_ms
#             except ValueError:
#                 continue
        
#         logger.error(f"   [!! ERROR] Date format not understood: {date_str}")
#         return None

#     def fetch_telemetry(self, keyword, start_ts, end_ts):
#         logger.info(f"[>> ENTER fetch_telemetry] Looking for '{keyword}' between timestamps {start_ts} and {end_ts}")

#         if not os.path.exists(self.data_file):
#             logger.error(f"[!! ERROR] File not found at: {self.data_file}")
#             return []

#         formatted_list = []
        
#         # Statistics counters for logging
#         stats = {"total_rows": 0, "skipped_header": 0, "skipped_keyword": 0, "skipped_date": 0, "valid": 0, "errors": 0}

#         logger.info(f"   [Action] Opening CSV file: {self.data_file}")

#         with open(self.data_file, 'r') as f:
#             reader = csv.reader(f)
            
#             try:
#                 header = next(reader) # Skip header
#                 stats["skipped_header"] = 1
#             except StopIteration:
#                 logger.warning("   [!! WARNING] CSV file is empty.")
#                 return []

#             for row in reader:
#                 stats["total_rows"] += 1
                
#                 # Check for malformed rows
#                 if len(row) < 4: 
#                     stats["errors"] += 1
#                     continue 
                
#                 # Extract raw data
#                 row_mac = row[0].strip()
#                 row_type = row[1].strip() 
#                 row_time = row[2].strip()  
#                 row_val  = row[3].strip() 

#                 # Filter 1: Keyword Check
#                 if row_type != keyword: 
#                     stats["skipped_keyword"] += 1
#                     continue

#                 try:
#                     # Convert CSV time to timestamp (ms)
#                     dt_obj = datetime.fromisoformat(row_time)
#                     row_ts = dt_obj.timestamp() * 1000 
#                     value = float(row_val)
                    
#                     # Filter 2: Date Range Check
#                     if start_ts <= row_ts <= end_ts:
#                         formatted_list.append({"ts": row_ts, "value": value})
#                         stats["valid"] += 1
#                     else:
#                         stats["skipped_date"] += 1
                        
#                 except (ValueError, TypeError) as e:
#                     stats["errors"] += 1
#                     continue

#         # Sort the results
#         formatted_list.sort(key=lambda x: x['ts'])

#         # --- DETAILED SUMMARY LOG ---
#         logger.info(f"   [Summary] Total Data Rows Scanned: {stats['total_rows']}")
#         logger.info(f"   [Summary] Skipped (Wrong Keyword): {stats['skipped_keyword']}")
#         logger.info(f"   [Summary] Skipped (Out of Date Range): {stats['skipped_date']}")
#         logger.info(f"   [Summary] Skipped (Parse Errors): {stats['errors']}")
#         logger.info(f"   [Summary] VALID DATA KEPT: {stats['valid']}")
        
#         logger.info(f"[<< EXIT fetch_telemetry] Returning {len(formatted_list)} records.")
#         return formatted_list

#     def visualize_telemetry(self, title, data):
#         logger.info(f"[>> ENTER visualize_telemetry] Title: '{title}', Data Points: {len(data)}")

#         if not data:
#             logger.warning("   [!! WARNING] No data provided to plot. Aborting visualization.")
#             return

#         timestamps = []
#         values = []

#         logger.info("   [Action] Preparing data for plotting (converting ms to datetime objects)...")
#         for entry in data:
#             ts = entry["ts"] / 1000  
#             dt = datetime.fromtimestamp(ts)
#             timestamps.append(dt)
#             values.append(entry["value"])

#         # Plotting
#         plt.figure(figsize=(10, 6))
#         plt.plot(timestamps, values, marker='o', linestyle='-', color='red', label='Sensor Value')
#         plt.title(title)
#         plt.xlabel("Time")
#         plt.ylabel("Value")
#         plt.legend()
#         plt.grid(True)
        
#         # Formatting X Axis
#         plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
#         plt.xticks(rotation=45)
#         plt.tight_layout()

#         # Filename Generation
#         current_time_str = datetime.now().strftime("%Y%m%d_%H%M%S")
#         safe_title = title.replace(" ", "_")
#         filename = f"{safe_title}_{current_time_str}.png"

#         script_dir = os.path.dirname(os.path.abspath(__file__))
#         output_path = os.path.join(script_dir, filename)
        
#         plt.savefig(output_path)
#         plt.close()

#         logger.info(f"   [Output] Graph file created at: {output_path}")
#         logger.info(f"[<< EXIT visualize_telemetry] Visualization complete.")

#     def process_sensors_visualize(self, keyword, start_date, end_date, title):
#         logger.info("="*60)
#         logger.info(f"[>> ENTER process_sensors_visualize] Orchestrating workflow.")
#         logger.info(f"   Params -> Keyword: {keyword} | Start: {start_date} | End: {end_date}")

#         # Step 1: Convert Dates
#         start_ts = self.date_to_timestamp(start_date)
#         end_ts = self.date_to_timestamp(end_date)

#         if start_ts is None or end_ts is None:
#             logger.error("[!! CRITICAL] Date conversion failed. Stopping process.")
#             return
        
#         # Step 2: Fetch Data
#         telemetry_data = self.fetch_telemetry(keyword, start_ts, end_ts)
        
#         # Step 3: Visualize
#         self.visualize_telemetry(title, telemetry_data)
        
#         logger.info(f"[<< EXIT process_sensors_visualize] Workflow finished.")
#         logger.info("="*60)

# # --- EXECUTION BLOCK ---
# if __name__ == "__main__":
#     print("\n--- PROGRAM STARTING ---\n")
    
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     csv_path = os.path.join(script_dir, "sensor_data.csv")
    
#     processor = SensorProcessor(data_file=csv_path)

#     processor.process_sensors_visualize(
#         keyword="co2",
#         start_date="2026-01-30",
#         end_date="2026-01-31",
#         title="CO2 Sensor Data")
#     print("\n--- PROGRAM ENDED ---\n")

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import csv
import logging
import os
import sys

# --- Logger Ayarları ---
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

class SensorProcessor:

    def __init__(self, data_file):
        self.data_file = data_file
        logger.info(f"[__init__] SensorProcessor baslatildi. Hedef Dosya: {self.data_file}")

    def date_to_timestamp(self, date_str):
        # Tarih formatlarini dener
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                dt_obj = datetime.strptime(date_str, fmt)
                return dt_obj.timestamp() * 1000 
            except ValueError:
                continue
        logger.error(f"Tarih formati anlasilamadi: {date_str}")
        return None

    def fetch_telemetry(self, keyword, start_ts, end_ts):
        logger.info(f"[>> GIRIS fetch_telemetry] '{keyword}' araniyor...")

        if not os.path.exists(self.data_file):
            logger.error(f"[!! HATA] Dosya bulunamadi: {self.data_file}")
            return []

        formatted_list = []
        
        # Istatistik sayaclari
        stats = {"toplam_satir": 0, "baslik_atlandi": 0, "keyword_uyusmadi": 0, "tarih_disi": 0, "gecerli": 0, "hata": 0}

        with open(self.data_file, 'r') as f:
            reader = csv.reader(f)
            
            try:
                header = next(reader) # Baslik satirini atla
                stats["baslik_atlandi"] = 1
            except StopIteration:
                return []

            for row in reader:
                stats["toplam_satir"] += 1
                
                if len(row) < 4: 
                    stats["hata"] += 1
                    continue 
                
                row_type = row[1].strip() 
                row_time = row[2].strip()  
                row_val  = row[3].strip() 

                if row_type != keyword: 
                    stats["keyword_uyusmadi"] += 1
                    continue

                try:
                    dt_obj = datetime.fromisoformat(row_time)
                    row_ts = dt_obj.timestamp() * 1000 
                    value = float(row_val)
                    
                    if start_ts <= row_ts <= end_ts:
                        formatted_list.append({"ts": row_ts, "value": value})
                        stats["gecerli"] += 1
                    else:
                        stats["tarih_disi"] += 1
                        
                except (ValueError, TypeError):
                    stats["hata"] += 1
                    continue

        formatted_list.sort(key=lambda x: x['ts'])

        logger.info(f"   [Ozet] Toplam Taranan: {stats['toplam_satir']}")
        logger.info(f"   [Ozet] GECERLI VERI SAYISI: {stats['gecerli']}")
        
        return formatted_list

    def visualize_telemetry(self, title, data):
        logger.info(f"[>> GIRIS visualize_telemetry] Grafik ciziliyor: '{title}' ({len(data)} veri noktasi)")

        if not data:
            logger.warning("   [!! UYARI] Cizilecek veri yok.")
            return

        timestamps = []
        values = []

        for entry in data:
            ts = entry["ts"] / 1000  
            dt = datetime.fromtimestamp(ts)
            timestamps.append(dt)
            values.append(entry["value"])

        # Grafigi Ciz
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, values, marker='o', linestyle='-', color='blue', label=title)
        plt.title(title)
        plt.xlabel("Zaman")
        plt.ylabel("Deger")
        plt.legend()
        plt.grid(True)
        
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.xticks(rotation=45)
        plt.tight_layout()

        # --- YENI KAYIT MANTIGI ---
        # 1. Kodun oldugu yerde 'graphs' diye bir klasor yolu belirle
        script_dir = os.path.dirname(os.path.abspath(__file__))
        graph_folder = os.path.join(script_dir, "graphs")

        # 2. Eger bu klasor yoksa OLUSTUR
        if not os.path.exists(graph_folder):
            os.makedirs(graph_folder)
            logger.info(f"   [Bilgi] Yeni klasor olusturuldu: {graph_folder}")

        # 3. Dosya ismini belirle (Tarih ve Saat ile)
        current_time_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_title = title.replace(" ", "_")
        filename = f"{safe_title}_{current_time_str}.png"

        # 4. Grafigi bu klasorun icine kaydet
        output_path = os.path.join(graph_folder, filename)
        
        plt.savefig(output_path)
        plt.close()

        logger.info(f"   [CIKIS] Grafik su klasore kaydedildi -> {output_path}")
        logger.info(f"[<< CIKIS visualize_telemetry] Islem tamam.")

    def process_sensors_visualize(self, keyword, start_date, end_date, title):
        logger.info("="*60)
        logger.info(f"[>> ISLEM BASLIYOR] Parametreler: {keyword} | {start_date} -> {end_date}")

        start_ts = self.date_to_timestamp(start_date)
        end_ts = self.date_to_timestamp(end_date)

        if start_ts is None or end_ts is None:
            return
        
        telemetry_data = self.fetch_telemetry(keyword, start_ts, end_ts)
        self.visualize_telemetry(title, telemetry_data)
        logger.info("="*60)

# --- CALISTIRMA ---
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