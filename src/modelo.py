import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Cargar el modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

def preprocess_text(text):
    """
    Función para limpiar y normalizar el texto:
    - Convierte a minúsculas
    - Elimina caracteres especiales y puntuación
    - Tokeniza y lematiza
    - Elimina stopwords
    """
    text = text.lower()  # Convertir a minúsculas
    text = re.sub(r"[^a-záéíóúüñ ]", "", text)  # Eliminar caracteres especiales y puntuación
    doc = nlp(text)  # Procesar con spaCy
    tokens = [token.lemma_ for token in doc if not token.is_stop]  # Lematización y eliminación de stopwords
    return " ".join(tokens)

# Definir un conjunto de mensajes de entrenamiento
corpus = [
    "Hola, ¿cómo estás?",
    "¿Cuál es el precio del servicio?",
    "Necesito ayuda con mi cuenta.",
    "Gracias, muy amable."
]

# Etiquetas de entrenamiento (asociadas a cada frase del corpus anterior)
y = [0, 1, 2, 3]  # 0 = saludo, 1 = precio, 2 = ayuda, 3 = agradecimiento

# Preprocesar los mensajes antes de vectorizar
corpus_clean = [preprocess_text(mensaje) for mensaje in corpus]

# Crear y entrenar el vectorizador TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus_clean)

# Entrenar el modelo de Naïve Bayes
clf = MultinomialNB()
clf.fit(X, y)

# Función para clasificar un nuevo mensaje
def classify_message(text):
    """
    Clasifica un mensaje basado en el modelo Naïve Bayes entrenado
    """
    clean_text = preprocess_text(text)  # Preprocesar el mensaje
    X_new = vectorizer.transform([clean_text])  # Convertir a vector TF-IDF
    prediction = clf.predict(X_new)[0]  # Clasificar
    return prediction

# Prueba con un nuevo mensaje
test_message = "¿Cuánto cuesta el servicio?"
prediction = classify_message(test_message)
print(f"Categoría predicha: {prediction}")






'''
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Cargar el modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

def preprocess_text(text):
    """
    Función para limpiar y normalizar el texto:
    - Convierte a minúsculas
    - Elimina caracteres especiales y puntuación
    - Tokeniza y lematiza
    - Elimina stopwords
    """
    text = text.lower()  # Convertir a minúsculas
    text = re.sub(r"[^a-záéíóúüñ ]", "", text)  # Eliminar caracteres especiales y puntuación
    doc = nlp(text)  # Procesar con spaCy
    tokens = [token.lemma_ for token in doc if not token.is_stop]  # Lematización y eliminación de stopwords
    return " ".join(tokens)

# Definir un conjunto de mensajes de entrenamiento
corpus = [
    "Hola, ¿cómo estás?",
    "¿Cuál es el precio del servicio?",
    "Necesito ayuda con mi cuenta.",
    "Gracias, muy amable."
]

# Preprocesar los mensajes antes de vectorizar
corpus_clean = [preprocess_text(mensaje) for mensaje in corpus]

# Crear y entrenar el vectorizador TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus_clean)

# Mostrar los términos y sus valores en TF-IDF
print("Términos en TF-IDF:", vectorizer.get_feature_names_out())
print("Matriz TF-IDF:\n", X.toarray())

# Función para vectorizar un nuevo mensaje
def vectorize_message(text):
    """
    Convierte un mensaje en su representación numérica con TF-IDF
    """
    clean_text = preprocess_text(text)  # Preprocesar el mensaje
    return vectorizer.transform([clean_text])  # Convertir a vector TF-IDF

# Prueba con un nuevo mensaje
test_message = "Quisiera saber el costo del servicio."
test_vector = vectorize_message(test_message)
print("Vector del mensaje de prueba:", test_vector.toarray())
'''