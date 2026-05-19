from flask import render_template

def list(usuarios):
    return render_template("usuarios/login.html")


def login():
    return render_template("usuarios/login.html")


def register():
    return render_template("usuarios/register.html")