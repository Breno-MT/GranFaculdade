import matplotlib.pyplot as plt

class Campanha:
    def __init__(self, canal, investimento, cliques, conversoes):
        self.canal = canal
        self.investimento = investimento
        self.cliques = cliques
        self.conversoes = conversoes

    def custo_per_click(self):
        return self.investimento / self.cliques

campanhas = [
    Campanha('Facebook Ads', 1000, 15000, 150),
    Campanha('Google Ads', 1200, 10000, 200),
    Campanha('Email Ads', 5000, 5000, 50),
    Campanha('Instagram Ads', 800, 12000, 80),
]

canais = [c.canal for c in campanhas]
custos_per_click = [c.custo_per_click() for c in campanhas]

plt.bar(canais, custos_per_click)
plt.title('Custos por Clique')
plt.xlabel('Canais')
plt.ylabel('Custo em Reais R$')
plt.show()
