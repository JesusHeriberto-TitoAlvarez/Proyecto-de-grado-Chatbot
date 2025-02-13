from nlp.classifier import classify_message

# Definir respuestas según categoría
RESPUESTAS = {
    0: "¡Hola! ¿En qué puedo ayudarte creador todo poderoso?",
    1: "Nuestros precios varían según el servicio. ¿Quieres más detalles? Aunque para ti es gratis",
    2: "Puedes contactar a soporte en nuestro sitio web. O encontraremos otra manera",
    3: "¡De nada! Estoy aquí para ayudar querido creador."
}

def get_response(text):
    """Clasifica el mensaje y devuelve una respuesta adecuada."""
    category = classify_message(text)
    return RESPUESTAS.get(category, "Lo siento, no entendí tu mensaje.")
