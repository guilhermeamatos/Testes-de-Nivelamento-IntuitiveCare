from flask import Flask
from flask_cors import CORS
from routes.search import search_bp

app = Flask(__name__)
CORS(app)  # Permite requisições de outras origens (CORS)

app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)
