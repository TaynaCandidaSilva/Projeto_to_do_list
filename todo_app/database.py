from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'postgresql://postgres:senha123@localhost:5432/todo_db?application_name=MeuGerenciadorDeTarefas'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'max_overflow': 5,
    'pool_timeout': 30,
    'pool_recycle': 1800
}

db = SQLAlchemy(app)
