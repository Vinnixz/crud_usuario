"""
Este módulo fornece funções para criar uma conexão com um banco de dados SQLite
e criar uma tabela de usuários.
"""
import sqlite3
from core.logs.logger import setup_logger

logger = setup_logger(__name__)

def create_connection():
    "Cria a conexão do banco"
    connection = None
    try:
        connection = sqlite3.connect("crud.db")
        logger.info("Conexão com a tabela criada com sucesso")
    except sqlite3.Error as database_error:
        logger.info("O erro '%s' ocorreu", database_error)
    return connection


def create_table(connection):
    "Cria uma tabela com id, nome, email e senha do usuário"
    query = """
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        logger.info("Tabela 'user' criada com sucesso")
    except sqlite3.Error as database_error:
        logger.info("O erro '%s' ocorreu", database_error)


def main():
    "Cria conexão com o banco"
    connection = create_connection()
    if connection:
        create_table(connection)
        connection.close()


if __name__ == "__main__":
    main()
