"""
Rotas de acesso do usuário
"""

from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from core.logs.logger import setup_logger
from core.services.controllers.access import AccessController
from core.services.database.access import (
    AccessDB,
)

logger = setup_logger(__name__)
access_blueprint = Blueprint("access", __name__)


dao = AccessDB()
access_controller = AccessController(dao)


@access_blueprint.route("/")
def alive():
    "Vê se o servidor está funcionando"
    return render_template("index.html")


@access_blueprint.route("/show_register", methods=["GET"])
def show_register():
    "Mostra a tela de registrar"
    return render_template("index.html")

@access_blueprint.route("/show_success_register")
def show_success_register():
    "Mostra tela de cadastro com sucesso"
    return render_template("register.html")

@access_blueprint.route("/register", methods=["POST"])
def register():
    "Processa o formulário de registro"
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    response, status_code = access_controller.create_user(username, password, email)

    if status_code == 201:
        return redirect(url_for("access.show_success_register"))
    return jsonify(response), 400


