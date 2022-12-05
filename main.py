from flask import Flask, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)


@app.context_processor
def date_now():

    return {
        'fecha': datetime.utcnow()
    }


@app.route('/')
def index():
    edad = 15
    personas = ['Nachowski', 'Pacowski', 'Juanchowski', 'Manolowski']
    return render_template('index.html',
                           edad=edad,
                           dato1='Valor',
                           dato2='Valor2',
                           lista=['uno', 'dos', 'tres'],
                           personas=personas
                           )


@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<string:apellidos>')
def informacion(nombre=None, apellidos=None):
    texto = ''
    if nombre != None and apellidos != None:
        texto = f'<h3>Bienvenido, {nombre} {apellidos}</h3>'
    return render_template('informacion.html', texto=texto)


@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion=None):
    if redireccion != None:
        return redirect(url_for('lenguajes'))
    return render_template('contacto.html')


@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template('lenguajes.html')


if __name__ == '__main__':
    app.run(debug=True)