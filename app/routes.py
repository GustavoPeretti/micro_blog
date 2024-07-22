from app import app
from flask import render_template, request

class Usuario:
    def __init__(self, nome, descricao, status):
        self.nome = nome
        self.descricao = descricao
        self.status = status

usuario = Usuario('Gustavo', 'Aluno do IFC', True)
usuarios = [Usuario('Galileu Galilei', 'negocio é heliocentrismo', True), Usuario('Charles Darwin', 'os que mais se adapta sobrevive', False), Usuario('Tchaikovsky', 'quebra nozes', False)]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', dados={'usuario': usuario, 'usuarios': usuarios})

@app.route('/contatos')
def contato():
    return render_template('contatos.html', contatos=[])