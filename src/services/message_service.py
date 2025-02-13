import requests
from config import ACCESS_TOKEN, PHONE_NUMBER_ID

def send_message(recipient_id, text):
    """Envía un mensaje a través de la API de WhatsApp."""
    url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_id,
        "type": "text",
        "text": {"body": text}
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Error al enviar el mensaje: {response.text}")
    else:
        print("Mensaje enviado correctamente.")
