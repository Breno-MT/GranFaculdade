from models.AbstractCrud import AbstractCrud

class Produto(AbstractCrud):
    arquivo = 'db/produtos.json'

    def __init__(self, codigo, nome, quantidade = 0, valor = 0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def inserir(self):
        lista = self.consultar()
        produto_duplicado = filter(lambda x: x['codigo'] == self.codigo, lista)

        if (len(list(produto_duplicado))):
            print()
            print('Já existe um produto com esse codigo.')
        else:
            super().inserir()
    