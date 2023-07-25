import requests
import json

class WhatsApp:
    def __init__(self):
        self.base_url = 'http://18.231.180.54:8000'

    def send_message(self, message, phone_to_send):
        message_data = {
            "number": f"55{phone_to_send}",
            "message": message
        }
        print("WHATS=>", message, phone_to_send)

        response = requests.post(self.base_url, json=json.dumps(message_data))
        return response