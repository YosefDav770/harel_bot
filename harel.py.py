import requests

# Connection Credentials
ID_INSTANCE = "7103509026"
API_TOKEN = "f3287939491e4f0abc8e2deca49b6a5e86e16f6095c14b74a8"

def send_message(phone_number, text):
    url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"
    payload = {
        "chatId": f"{phone_number}@c.us",
        "message": text
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    print("Harel's Rings Bot is online!")
    # Example message
    # send_message("972XXXXXXXXX", "Hello! This is Harel's Bot.")
