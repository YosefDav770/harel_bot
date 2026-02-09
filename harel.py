import requests

ID_INSTANCE = "7103509946"
API_TOKEN = "16176ae214c442d2b8a14fbf5ad5f1503bc7d30cb0be416e88"

def send_message(phone, text):
    url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"
    payload = {"chatId": f"{phone}@c.us", "message": text}
    requests.post(url, json=payload)



if __name__ == "__main__":
    print("Bot is running!")
    send_message(".c.us@972509902568", "Hello! The bot is working!")








