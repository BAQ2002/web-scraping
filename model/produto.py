class Produto:
    def __init__(self, titulo, preco):
        self.titulo = titulo
        self.preco = preco

    def __str__(self):
        return f"Produto(titulo='{self.titulo}', preco='{self.preco}')"
