"""
Rotas de acesso do usuário
"""

from flask import Blueprint, request, jsonify
from core.logs.logger import setup_logger

logger = setup_logger(__name__)
access_blueprint = Blueprint("access", __name__)

@access_blueprint.route("/")
def alive():
    "Vê se o servidor está funcionando"
    return "<h1>ALIVE</h1>"