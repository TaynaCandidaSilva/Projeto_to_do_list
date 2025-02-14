from flask import Blueprint, request, render_template
from database import db
from models import Tarefa

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET", "POST"])
def criar_tarefa():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = "Descrição da tarefa" 
        concluida = False

        nova_tarefa = Tarefa(titulo, descricao, concluida)

        db.session.add(nova_tarefa)
        db.session.commit()

    tarefas = Tarefa.query.all()

    return render_template("index.html", tarefas=tarefas)
