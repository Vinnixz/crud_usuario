"""
Módulo que gerencia o usuário no banco de dados
"""

import sqlite3


class AgenteDB:
    "Inicia banco do usuário"

    def __init__(self, db_path="meuapp.db"):
        self.db_path = db_path

    def adiciona_usuario(self, username, senha):
        "Adiciona um usuário novo"
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO usuario (username, senha) VALUES (?, ?)", (username, senha)
        )
        connection.commit()
        connection.close()

    def check_login(self, username, senha):
        "Verifica se o login da pessoa existe no banco"
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?", (username, senha)
        )
        user = cursor.fetchone()
        connection.close()
        return user
