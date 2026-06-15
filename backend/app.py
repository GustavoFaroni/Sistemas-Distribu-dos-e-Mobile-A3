import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from models import db
from routes import api_blueprint

load_dotenv()

def criar_app():
    app = Flask(__name__)
    CORS(app)

    url_banco = os.getenv('DATABASE_URL')
    if url_banco and url_banco.startswith("postgres://"):
        url_banco = url_banco.replace("postgres://", "postgresql://", 1)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = url_banco or 'postgresql://postgres:postgres@localhost:5432/veiculos_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(api_blueprint, url_prefix='/api')

    with app.app_context():
        try:
            db.create_all()
            print("Banco de dados inicializado com sucesso.")
        except Exception as e:
            print(f"Erro ao inicializar banco de dados: {e}")

    return app

if __name__ == '__main__':
    app = criar_app()
    app.run(debug=True, port=5000)
