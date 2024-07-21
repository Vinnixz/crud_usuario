"""
Este módulo fornece funções para criar uma conexão com um banco de dados SQLite
e criar uma tabela de usuários.
"""
import sqlite3


def create_connection():
    "Cria a conexão do banco"
    connection = None
    try:
        connection = sqlite3.connect("meuapp.db")
        print("Connection to SQLite DB successful")
    except sqlite3.Error as database_error:
        print(f"The error '{database_error}' occurred")
    return connection


def create_table(connection):
    "Cria uma tabela com id, nome, email e senha do usuário"
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
        email TEXT NOT NULL UNIQUE
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Table created successfully")
    except sqlite3.Error as database_error:
        print(f"The error '{database_error}' occurred")


def main():
    "Cria conexão com o banco"
    connection = create_connection()
    if connection:
        create_table(connection)
        connection.close()


if __name__ == "__main__":
    main()