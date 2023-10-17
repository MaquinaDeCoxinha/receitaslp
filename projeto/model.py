# banco de dados
from app import mongo

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Receita:
    def __init__(self, userid, titulo, tags, conteudo):
        self.user = userid
        self.titulo = titulo
        self.tags = tags
        self.conteudo = conteudo
