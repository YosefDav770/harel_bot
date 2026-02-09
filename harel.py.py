OPENAI_KEY = "sk-proj-c6LvGRqz6wSJ36UOU51iFXKE2bdRWQVreOYfb2tB8WVEsyZ9rFYc1jy2j8oj5sfhfl-OlrufT38lbkFJcJJ_969dUIBKKb0p7Cdtkmsjj2Frp1eZ9JDr-QKLqYaYjscKxtTEuR7TkOEao6Rl9NkzJoelA"
ACCESS_TOKEN = "EAAQnr42ZAp9cBQjbMZAKLLZCBPKVEEpdlisHkaJ8rWi0ZBphbBKsF0AwZCXxmVzTn44mvr1XgPUrF5E2EjzYZCm3FgMLLZBcl3z2FZBSFD2qwUZCXa7G3ZCZBcT7yGD0JJ03Xnr58mZBwrOyZCFkcHFmZAAV6TgKWbKcUZCZAm8UppEYPgEO4UVU2ZAaedYoCuxaYL2NPSahCQMj3qUmD0UYN64mFfncv0IXAv1Nbz6iuEfqZBmQQzaKn4eZB6nEkcKZCQZDZD"
PHONE_ID = "958301674038546"
VERIFY_TOKEN = "harel123"

import requests
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=OPENAI_KEY)

def send_whatsapp_message(recipient, text):
    url = f"https://graph.facebook.com/v18.0/{PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": recipient,
        "type": "text",
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=data)

@app.route("/", methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Verification failed", 403

    data = request.json
    try:
        msg_body = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg_body}]
        )
        answer = response.choices[0].message.content
        send_whatsapp_message(sender, answer)
        return "ok", 200
    except:
        return "ok", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)