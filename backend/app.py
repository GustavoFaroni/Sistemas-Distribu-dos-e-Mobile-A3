import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from models import db
from routes import api_blueprint

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuration
    database_url = os.getenv('DATABASE_URL')
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'postgresql://postgres:postgres@localhost:5432/veiculos_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db with app
    db.init_app(app)

    # Register routes
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # Create tables
    with app.app_context():
        try:
            db.create_all()
            print("Banco de dados inicializado com sucesso.")
        except Exception as e:
            print(f"Erro ao inicializar banco de dados: {e}")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
