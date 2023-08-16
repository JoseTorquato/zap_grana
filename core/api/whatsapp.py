import requests
import json

class WhatsApp:
    def __init__(self):
        self.base_url = 'http://52.67.244.232:8000/'

    def send_message(self, message, phone_to_send):
        if len(phone_to_send) == 11:
            ddd_number = int(phone_to_send[:2])

            if not 11 <= ddd_number <= 27:
                phone_to_send = phone_to_send[:2]+phone_to_send[3:]
                
        message_data = {
            "number": f"55{phone_to_send}",
            "message": message
        }

        header = {"Content-Type": "application/json"}
        response = requests.post(f"{self.base_url}/send-message", data=json.dumps(message_data), headers=header)
        return response