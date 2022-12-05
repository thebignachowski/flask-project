from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)


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


@app.route('/crear-coche', methods=['GET', 'POST'])
def crear_coche():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        local = request.form['local']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)",
                       (marca, modelo, precio, local))
        cursor.connection.commit()
        return redirect(url_for('index'))

    return render_template('crear_coche.html')


if __name__ == '__main__':
    app.run(debug=True)
