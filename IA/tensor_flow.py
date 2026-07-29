import tensorflow as tf

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

produtos = [
    Produto('Camiseta', 29.99, 'Roupas'),
    Produto('Calças Jeans', 79.99, 'Roupas'),
    Produto('Tênis', 99.99, 'Calçados'),
    Produto('Celular', 1499.99, 'Eletronico'),
    Produto('Notebook', 3499.99, 'Eletronico'),
    Produto('Livro', 19.99, 'Livros'),
]

nomes = tf.constant([p.nome for p in produtos])
precos = tf.constant([p.preco for p in produtos])
categorias = tf.constant([p.categoria for p in produtos])
media = tf.reduce_mean(precos)
eletronicos = tf.boolean_mask(nomes, tf.equal(categorias, 'Eletronico'))

print(media)
print(eletronicos)
