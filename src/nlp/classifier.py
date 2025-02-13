from sklearn.svm import SVC
from nlp.vectorizer import X, transform_text
from nlp.dataset import labels

# Entrenar modelo SVM
clf = SVC(kernel="linear")
clf.fit(X, labels)

def classify_message(text):
    """Clasifica un mensaje basado en el modelo SVM."""
    X_new = transform_text(text)
    prediction = clf.predict(X_new)[0]
    return prediction