from flask import Blueprint, redirect, request, render_template, url_for, jsonify
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

@routes.route('/atualizar_tarefa/<int:tarefa_id>', methods=['POST'])
def atualizar_tarefa(tarefa_id):
    data = request.get_json()
    tarefa = Tarefa.query.get(tarefa_id)

    if not tarefa:
        return jsonify({"success": False, "error": "Tarefa não encontrada"}), 404

    tarefa.concluida = data.get("concluida", False)
    db.session.commit()

    return jsonify({"success": True})

@routes.route('/tarefas/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
   
    tarefa = Tarefa.query.get_or_404(id)
    if request.method == 'POST':
        tarefa.titulo = request.form['titulo']
        db.session.commit()
        return redirect(url_for('routes.criar_tarefa'))  
    return render_template('editar_tarefa.html', tarefa=tarefa)

@routes.route('/excluir_tarefa/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    try:
        tarefa = Tarefa.query.get_or_404(id)
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({"success": True, "message": "Tarefa excluída com sucesso!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Falha ao excluir tarefa"
        }), 500