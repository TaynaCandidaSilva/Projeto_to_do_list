from database import db

class Tarefa(db.Model):
    __tablename__ = 'tasks'

    id_tarefa = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=True)
    concluida = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, titulo, descricao, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida
    
    def __dicionario__(self):
        return {
            "id_tarefa": self.id_tarefa,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida
        }

    