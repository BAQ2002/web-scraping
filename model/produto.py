class Produto:
    def __init__(self, titulo, preco):
        self.titulo = titulo
        self.preco = preco

    def __repr__(self):
        return f"Produto(titulo={self.titulo}, preco={self.preco})"