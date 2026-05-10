import paho.mqtt.client as mqtt
import os
import time

# ĐÃ SỬA: Phải lấy tên biến từ file YAML/Secrets, không phải điền giá trị trực tiếp ở đây
MQTT_SERVER = os.getenv('MQTT_SERVER')
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASS = os.getenv('MQTT_PASS')

def send_response():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.tls_set() 
    
    try:
        # Nếu MQTT_SERVER bị None (do chưa cài Secret), sẽ báo lỗi rõ ràng
        if not MQTT_SERVER:
            raise ValueError("Lỗi: Chưa cấu hình MQTT_SERVER trong GitHub Secrets!")

        print(f"Đang kết nối tới {MQTT_SERVER}...")
        client.connect(MQTT_SERVER, 8883)
        
        message = "XÁC NHẬN: Python từ GitHub Server đã phản hồi thành công!"
        client.publish("web/test/response", message)
        
        print("Đã gửi phản hồi thành công!")
        time.sleep(2) 
        client.disconnect()
    except Exception as e:
        print(f"Lỗi kết nối MQTT: {e}")

if __name__ == "__main__":
    send_response()
