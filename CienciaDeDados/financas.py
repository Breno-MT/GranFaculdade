import pandas as pd
import matplotlib.pyplot as plt

class Investimentos:
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome
        self.valor = valor
        self.taxa = taxa
        self.periodo = periodo

investimentos = {
    "investimento_1": Investimentos('Tesouro Direto', 10000, 0.02, 5),
    "investimento_2": Investimentos('Ações', 5000, 0.05, 3),
    "investimento_3": Investimentos('Poupança', 8000, 0.01, 10),
    "investimento_4": Investimentos('CDB', 15000, 0.03, 7),
}

l_investimentos = [i.__dict__ for i in investimentos.values()]

df_investimentos = pd.DataFrame.from_records(l_investimentos, index=investimentos.keys())
df_investimentos['Retorno'] = df_investimentos.apply(lambda l: l.valor * (1 + l.taxa) ** l.periodo, axis=1)

df_investimentos.plot(kind='bar', y='Retorno', legend='None')

plt.title('Retorno dos Investimentos')
plt.xlabel('Investimentos')
plt.ylabel('Retorno em Reais R$')
plt.show()

