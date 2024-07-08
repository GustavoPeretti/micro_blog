from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', dados={'nome': request.args.get('nome'), 'email': request.args.get('email')})

@app.route('/usuario/<nome>')
def usuario(nome):
    return nome

@app.route('/ano/<int:x>')
def ano(x):
    return 'Estamos no ' + str(x) + 'º ano.'

@app.route('/nota/<float:x>')
def nota(x):
    return f'Nota: {x}.'

@app.route('/media/<float:x>/<float:y>')
def media(x, y):
    return f'Média: {(x + y) / 2}.'

@app.route('/soma/<x>/<y>')
def soma(x, y):
    try:
        x = float(x)
        y = float(y)
    except:
        return 'Erro: forneça valores válidos.'
    return render_template('somar.html', dados={'x': x, 'y': y})