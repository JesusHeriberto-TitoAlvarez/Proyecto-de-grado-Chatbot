from services.message_service import send_message
from services.response_service import get_response

def process_message(sender_id, text):
    """Procesa un mensaje recibido, lo clasifica y envía una respuesta."""
    respuesta = get_response(text)
    send_message(sender_id, respuesta)
