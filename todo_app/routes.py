from flask import Blueprint, redirect, request, render_template, url_for
from database import db
from models import Tarefa

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET", "POST"])
def criar_tarefa():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        concluida = False

        nova_tarefa = Tarefa(titulo, concluida)

        db.session.add(nova_tarefa)
        db.session.commit()

        return redirect(url_for("routes.criar_tarefa"))

    tarefas = Tarefa.query.all()

    return render_template("index.html", tarefas=tarefas)
