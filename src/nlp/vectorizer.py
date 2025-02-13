from sklearn.feature_extraction.text import TfidfVectorizer
from nlp.preprocess import preprocess_text
from nlp.dataset import corpus

# Preprocesar y vectorizar el corpus
corpus_clean = [preprocess_text(text) for text in corpus]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus_clean)

def transform_text(text):
    """Convierte un texto en su representación numérica."""
    clean_text = preprocess_text(text)
    return vectorizer.transform([clean_text])