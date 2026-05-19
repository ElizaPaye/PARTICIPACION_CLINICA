from flask import request, redirect, url_for, Blueprint, session
from models.usuario_model import Usuario
from views import usuario_view
from datetime import datetime

usuario_bp = Blueprint('usuario', __name__, url_prefix="/usuarios")


@usuario_bp.route("/")
def index():
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)


@usuario_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        rol = request.form["rol"]

        if Usuario.get_by_username(username):
            return "Usuario ya existe"

        usuario = Usuario(username, password, rol)
        usuario.save()

        return redirect(url_for("usuario.login"))

    return usuario_view.register()


@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        usuario = Usuario.get_by_username(username)

        if usuario and usuario.check_password(password):
            session["user"] = usuario.username
            session["rol"] = usuario.rol
            return redirect(url_for("medico.index"))

        return "Credenciales incorrectas"

    return usuario_view.login()


@usuario_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("usuario.login"))