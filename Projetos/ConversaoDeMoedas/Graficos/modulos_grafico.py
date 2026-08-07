import matplotlib.pyplot as plt

def graficos_barra(l_moedas, l_valores):
    plt.bar(l_moedas, l_valores)
    plt.title('Conversão para REAL (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()

def graficos_pizza(l_valores, l_moedas):
    plt.pie(l_valores, labels=l_moedas)
    plt.title('Proporção em relação ao REAL (BRL)')
    plt.show()

def graficos_dispersao(l_moedas, l_valores):
    plt.scatter(l_moedas, l_valores)
    plt.title('Proporção em relação ao REAL (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()