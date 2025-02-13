from flask import Blueprint, request, jsonify
from database import db
from models import Tarefa

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()

    titulo = dados.get("titulo")
    descricao = dados.get("descricao")
    concluida = dados.get("concluida", False)

    nova_tarefa = Tarefa(titulo, descricao, concluida)

    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify({"mensagem": "Tarefa criada com sucesso!"}),201

