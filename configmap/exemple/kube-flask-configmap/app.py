from flask import Flask
import os

app = Flask(__name__)

# Lire depuis variable d'environnement avec valeur par défaut
PORT = int(os.environ.get("FLASK_PORT", 5001))

@app.route("/")
def hello():
    return f"Hello from Flask (read from file) on port {PORT}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)



# from flask import Flask

# app = Flask(__name__)

# with open("/config/FLASK_PORT") as f:
#     PORT = int(f.read().strip())
# @app.route("/")
# def hello():
#     return f"Hello from Flask (read from file) on port {PORT}"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=PORT)