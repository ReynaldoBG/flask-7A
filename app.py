from flask import Flask

from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hola, Mundo! 123456</p>"

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/alumnos/guardar", methods=["POST"])
def alumnosGuardar():
    matricula = request.form["txtMatriculaFA"]
    nombreApellido = request.form["txtNombreApellidoFA"]
    return f"Matrícula: {matricula} Nombre y Apellido: {nombreApellido}"
