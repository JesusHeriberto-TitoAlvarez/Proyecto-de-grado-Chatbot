from flask import Flask, request
import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

app = Flask(__name__)

@app.route("/")
def home():
    return "El chatbot está funcionando correctamente."

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        verify_token = request.args.get("hub.verify_token")
        if verify_token == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Token inválido", 403

    if request.method == "POST":
        data = request.get_json()
        if data and "entry" in data:
            for entry in data["entry"]:
                if "changes" in entry:
                    for change in entry["changes"]:
                        if "messages" in change["value"]:
                            message = change["value"]["messages"][0]
                            sender_id = message["from"]
                            message_text = message["text"]["body"]
                            send_message(sender_id, f"Recibí tu mensaje y le haremos copias en github. Acabo de jalar este codigo desde mi portatil: {message_text}")
        return "Evento recibido", 200

def send_message(recipient_id, text):
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


# import os
# from flask import Flask, request, jsonify
# from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
# load_dotenv()

# Configuración de variables de entorno
# ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
# VERIFY_TOKEN = "mi_token_seguro_123"  # Asegúrate de usar el mismo token en la configuración del Webhook en Meta
# PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

# Inicialización de la aplicación Flask
# app = Flask(__name__)

# Ruta principal para verificar si el servidor está activo
# @app.route("/", methods=["GET"])
# def home():
#     return "El servidor del chatbot está activo y funcionando correctamente."

# Ruta del Webhook (maneja la verificación y los eventos de mensajes entrantes)
# @app.route("/webhook", methods=["GET", "POST"])
# def webhook():
#     if request.method == "GET":
#         Verificación del Webhook
#         verify_token = request.args.get("hub.verify_token")
#         challenge = request.args.get("hub.challenge")

#         if verify_token == VERIFY_TOKEN:
#             return challenge, 200
#         return "Token de verificación inválido.", 403

#     elif request.method == "POST":
#         Procesar mensajes entrantes
#         data = request.get_json()
#         if data.get("entry"):
#             for entry in data["entry"]:
#                 if "changes" in entry:
#                     for change in entry["changes"]:
#                         if change.get("value").get("messages"):
#                             message = change["value"]["messages"][0]
#                             sender_id = message["from"]  # Número del remitente
#                             message_text = message["text"]["body"]  # Texto del mensaje

#                             Lógica de respuesta
#                             if message_text.lower() == "hola":
#                                 send_message(sender_id, "¡Hola! Soy un chatbot de prueba de Jesús Tito.")
#                             else:
#                                 send_message(sender_id, "Lo siento, no entiendo tu mensaje.")

#         return jsonify({"status": "received"}), 200

# Función para enviar mensajes de respuesta a través de la API de WhatsApp
# def send_message(recipient_id, text):
#     url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"
#     headers = {
#         "Authorization": f"Bearer {ACCESS_TOKEN}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "messaging_product": "whatsapp",
#         "to": recipient_id,
#         "type": "text",
#         "text": {"body": text}
#     }

#     response = requests.post(url, headers=headers, json=payload)
#     if response.status_code == 200:
#         print("Mensaje enviado correctamente.")
#     else:
#         print(f"Error al enviar el mensaje: {response.status_code} - {response.text}")

# Ejecutar la aplicación Flask
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True)
