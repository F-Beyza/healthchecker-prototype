

#def process_sensors_visualize(url, keyword):  #, start_date, end_date, title, mac_list):#
#    
#    # fetch_token() çağır
#    token = fetch_token(url)
#    
#
#    # sonraki fonksionu çağır
#    fetch_telemetry(url, keyword)
#
#def fetch_token(url):
#    #url parametresini yazdır
#    print("URL:", url)
#
#def fetch_telemetry(url, keyword):
#    # param1 yazdır
#    print("url:", url)
#    # param2 yazdır
#    print("keyword:", keyword)
#
#process_sensors_visualize(url="beyza", keyword="aaa")
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# def process_sensors_visualize(keyword, start_date, end_date, title, mac_list, url="https://api.test.com",):
#     print(url, keyword, start_date, end_date, title, mac_list)
    
#     fetch_token(url)

#     start_ts = date_to_timestamp(start_date)
#     end_ts = date_to_timestamp(end_date)

#     for mac_id in mac_list:
#         device_id = fetch_device_id(mac_id, url)
#         fetch_all_telemetry(mac_id, device_id, start_ts, end_ts)

# def fetch_token(url):
#     print(f"[fetch_token] url = {url}")

# def keyword_parser(keyword, mac_list):
#     print(f"[keyword_parser] keyword = {keyword}")
#     print(f"[keyword_parser] mac_list = {mac_list}")

# def date_to_timestamp(date_str):
#     print(f"[date_to_timestamp] date = {date_str}")
#     return 123456789  # dummy

# def fetch_device_id(mac_id, url):
#     print(f"[fetch_device_id] mac = {mac_id}, url = {url}")
#     return "dummy_device_id"

# def fetch_all_telemetry(mac_id, device_id, start_ts, end_ts):
#     print(f"[fetch_all_telemetry] mac={mac_id}, device={device_id}")
#     print(f"start={start_ts}, end={end_ts}")

# def visualize_telemetry(title):
#     print(f"[visualize_telemetry] title = {title}")

# process_sensors_visualize(
#        keyword="temperature",
#        start_date="2024-01-01",
#        end_date="2024-01-02",
#        title="Sensor Data",
#        mac_list=["AA:BB:CC", "11:22:33"]
#    )

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# class yapısı ekleyeceğiz, birden çok kez gönderilen veriyi hatırlar ve her seferinde bizim göndermemiz gerekmez
# class RemoteControl:
#     def __init__(self, brand):
#         self.brand = brand #hatırladığı bilgi
#         self.volume = 10 #state
#         #state+behavior=class

#     def volume_up(self):
#         self.volume += 1
#         print("Volume:", self.volume)

#     def volume_down(self):
#         self.volume -= 1
#         print("Volume:", self.volume)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

class SensorProcessor:

    def __init__(self, url):
        self.url = url

    def fetch_token(self):
        print(f"[fetch_token] url = {self.url}")

    def date_to_timestamp(self, date_str):
        print(f"[date_to_timestamp] date = {date_str}")
        return 123456789

    def fetch_device_id(self, mac_id):
        print(f"[fetch_device_id] mac = {mac_id}, url = {self.url}")
        return "dummy_device_id"

    def fetch_all_telemetry(self, mac_id, device_id, start_ts, end_ts):
        print(f"[fetch_all_telemetry] mac={mac_id}, device={device_id}")
        print(f"start={start_ts}, end={end_ts}")

    def visualize_telemetry(self, title):
        print(f"[visualize_telemetry] title = {title}")

    def process_sensors_visualize(self, keyword, start_date, end_date, title, mac_list):
        print("===process_sensors_visualize started ===")
        print("keyword:", keyword)
        print("mac_list:", mac_list)

        self.fetch_token()

        start_ts = self.date_to_timestamp(start_date)
        end_ts = self.date_to_timestamp(end_date)

        for mac_id in mac_list:
            device_id = self.fetch_device_id(mac_id)
            self.fetch_all_telemetry(mac_id, device_id, start_ts, end_ts)

        self.visualize_telemetry(title)

processor = SensorProcessor(url="https://api.test.com")

if __name__ == "__main__":
    processor.process_sensors_visualize(
        keyword="temperature",
        start_date="2024-01-01",
        end_date="2024-01-02",
    title="Sensor Data",
    mac_list=["AA:BB:CC", "11:22:33"]
)