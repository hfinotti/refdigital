from refdigital import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id):
    return Usuario.query.get(int(id))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True, unique=True)
    nome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

    # caso o nome do indice da tabela não seja id, esta função deve ser
    # criada para informar o nome do indice para o framework
    # def get_id(self):
    #     return str(self.id_usuario)

class Faq(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True, unique=True)
    titulo = database.Column(database.String, nullable=False)
    resposta = database.Column(database.Text, nullable=False)


class Servico(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True, unique=True)
    servico = database.Column(database.String, nullable=False)
    descricao = database.Column(database.String, nullable=False)


class Cliente(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True, unique=True)
    empresa = database.Column(database.String, nullable=False)
    nome = database.Column(database.String)
    cargo = database.Column(database.String)
    logo = database.Column(database.String, nullable=False, default='default.jpg')
    data_cadastro_cliente = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())


class Resultado(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True, unique=True)
    titulo = database.Column(database.String, nullable=False)
    texto_titulo = database.Column(database.String, nullable=False)
    subtitulo1 = database.Column(database.String)
    texto_subt1 = database.Column(database.String)
    subtitulo2 = database.Column(database.String)
    texto_subt2 = database.Column(database.String)
    subtitulo3 = database.Column(database.String)
    texto_subt3 = database.Column(database.String)

