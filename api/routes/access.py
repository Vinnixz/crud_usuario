"""
Rotas de acesso do usuário
"""

from flask import Blueprint, render_template
from core.logs.logger import setup_logger

logger = setup_logger(__name__)
access_blueprint = Blueprint("access", __name__)


@access_blueprint.route("/")
def alive():
    "Vê se o servidor está funcionando"
    return "<h1>ALIVE</h1>"

@access_blueprint.route("/show_register", methods=["GET"])
def show_register():
    "Mostra a tela de registrar"
    return render_template('index.html')
