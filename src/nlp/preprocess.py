import re
import spacy

# Cargar el modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

def preprocess_text(text):
    """
    Limpia y normaliza el texto:
    - Convierte a minúsculas
    - Elimina caracteres especiales y puntuación
    - Tokeniza y lematiza
    - Elimina stopwords
    """
    text = text.lower()
    text = re.sub(r"[^a-záéíóúüñ ]", "", text)  # Eliminar caracteres especiales y puntuación
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)