from sklearn.cluster import KMeans
import numpy as np

class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

produtos = [
    Produto('Produto 1', 60.50, 0.70),
    Produto('Produto 2', 15.67, 0.20),
    Produto('Produto 3', 70, 0.90),
    Produto('Produto 4', 2.99, 0.12),
    Produto('Produto 5', 120, 1.00),
    Produto('Produto 6', 90, 0.65),
]

precos = [[p.preco, p.peso] for p in produtos]
matriz = np.array(precos)

kmeans = KMeans(n_init='auto', n_clusters=4, random_state=0).fit(matriz)
print(kmeans)

labels = kmeans.labels_
print(labels)

for i in range(4):
    print(f"Grupo {i + 1}:")
    for j in range(len(produtos)):
        if labels[j] == i:
            print(" - ", produtos[j].nome)
