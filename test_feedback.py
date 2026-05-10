import paho.mqtt.client as mqtt
import os
import time

# Lấy dữ liệu từ GitHub Env
n1 = os.getenv('INPUT_N1')
n2 = os.getenv('INPUT_N2')
MQTT_SERVER = os.getenv('MQTT_SERVER')
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASS = os.getenv('MQTT_PASS')

def main():
    try:
        # Thực hiện phép tính
        result = float(n1) + float(n2)
        message = f"Phép tính: {n1} + {n2} = {result}"
        
        # Gửi phản hồi qua MQTT
        client = mqtt.Client()
        client.username_pw_set(MQTT_USER, MQTT_PASS)
        client.tls_set()
        client.connect(MQTT_SERVER, 8883)
        
        client.publish("web/test/response", message)
        print(f"Đã gửi kết quả: {message}")
        
        time.sleep(2)
        client.disconnect()
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
