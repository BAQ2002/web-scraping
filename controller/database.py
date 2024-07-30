import sqlite3
from datetime import datetime
from model.produto import Produto


class DatabaseManager:
    def __init__(self, db_name="produtos.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY,
                    titulo TEXT NOT NULL UNIQUE
                )
            """)
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS precos (
                    id INTEGER PRIMARY KEY,
                    produto_id INTEGER,
                    preco TEXT NOT NULL,
                    data_hora TEXT NOT NULL,
                    FOREIGN KEY (produto_id) REFERENCES produtos (id)
                )
            """)

    def salvar_produto(self, produto: Produto):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id FROM produtos WHERE titulo = ?", (produto.titulo,))
            produto_existente = cursor.fetchone()

            if produto_existente:
                produto_id = produto_existente[0]
            else:
                cursor.execute("INSERT INTO produtos (titulo) VALUES (?)", (produto.titulo,))
                produto_id = cursor.lastrowid

            self.salvar_preco(produto_id, produto.preco)

    def salvar_preco(self, produto_id, preco):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.connection:
            self.connection.execute(
                "INSERT INTO precos (produto_id, preco, data_hora) VALUES (?, ?, ?)",
                (produto_id, preco, data_hora)
            )

    # Consultar o banco e buscar pelo menor preço do dia com isso printar o nome do produto, o valor atual e sua variação.
    # Quero poder definir um valor a ser pago pelo produto. E que se o preco atual atingir um valor menor ou igual print(O valor definido foi atinido.)

    def fechar(self):
        self.connection.close()
