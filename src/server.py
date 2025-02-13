from flask import Flask
from routes import webhook_bp

app = Flask(__name__)

@app.route("/")
def home():
    return "El chatbot está funcionando correctamente."

# Registrar rutas desde routes.py
app.register_blueprint(webhook_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
