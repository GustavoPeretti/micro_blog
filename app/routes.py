from app import app
from flask import render_template, request, redirect, url_for, session

class Usuario:
    def __init__(self, nome, descricao, status):
        self.nome = nome
        self.descricao = descricao
        self.status = status

usuarios = [Usuario('Galileu Galilei', 'negocio é heliocentrismo', True), Usuario('Charles Darwin', 'os que mais se adapta sobrevive', False), Usuario('Tchaikovsky', 'quebra nozes', False)]

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    usuario = Usuario(request.args.get('usuario'), request.args.get('descricao'), True)
    return render_template('index.html', usuario=usuario, usuarios=usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        session['usuario'] = request.form.get('usuario')
        session['descricao'] = request.form.get('descricao')
        session['estado'] = request.form.get('estado')
        session['escolaridade'] = request.form.get('escolaridade')
        return redirect(url_for('index'))

@app.route('/contatos', methods=['GET'])
def contatos():
    return render_template('contatos.html', contatos=[])

