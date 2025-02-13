from flask import Blueprint, request, jsonify
from config import VERIFY_TOKEN
from chatbot import get_response, send_message

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        verify_token = request.args.get("hub.verify_token")
        if verify_token == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Token inválido", 403

    if request.method == "POST":
        try:
            data = request.get_json()
            if not data or "entry" not in data:
                return jsonify({"error": "Datos de entrada no válidos"}), 400

            for entry in data["entry"]:
                for change in entry.get("changes", []):
                    if "messages" in change.get("value", {}):
                        message = change["value"]["messages"][0]
                        sender_id = message.get("from")
                        message_text = message.get("text", {}).get("body")

                        if sender_id and message_text:
                            respuesta = get_response(message_text)
                            send_message(sender_id, respuesta)

            return "Evento recibido", 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
