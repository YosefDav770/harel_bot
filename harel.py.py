import requests

ID_INSTANCE = "7103509026"
API_TOKEN = "f3287939491e4f0abc8e2deca49b6a5e86e16f6095c14b74a8"

def send_message(phone, text):
    url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"
    payload = {"chatId": f"{phone}@c.us", "message": text}
    requests.post(url, json=payload)



if __name__ == "__main__":
    print("Bot is running!")
    send_message("972509902568@c.us", "Hello! The bot is working!")

