import paho.mqtt.client as mqtt
import os
import time

# Lấy thông tin từ GitHub Secrets (đã cấu hình trong file YAML)ggg
MQTT_SERVER = os.getenv('f7a99425c8a34f23aba171e48336da3b.s1.eu.hivemq.cloud')
MQTT_USER = os.getenv('long140203')
MQTT_PASS = os.getenv('Long140203')

def send_response():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.tls_set() # Sử dụng cổng 8883 bảo mật
    
    try:
        print(f"Đang kết nối tới {MQTT_SERVER}...")
        client.connect(MQTT_SERVER, 8883)
        
        # Gửi tin nhắn về topic mà Web đang lắng nghe
        message = "XÁC NHẬN: Python đã nhận lệnh và phản hồi thành công!"
        client.publish("web/test/response", message)
        
        print("Đã gửi phản hồi thành công!")
        time.sleep(2) # Đợi tin nhắn đi hẳn
        client.disconnect()
    except Exception as e:
        print(f"Lỗi kết nối MQTT: {e}")

if __name__ == "__main__":
    send_response()
