from moedas import get_cotacao
from ConversaoDeMoedas.Graficos.modulos_grafico import graficos_barra, graficos_pizza, graficos_dispersao

def menu():
    print()
    print('1 - Gráfico de Barra')
    print('2 - Gráfico de Pizza')
    print('3 - Gráfico de Dispersao')
    print('0 - Sair')
    print()


cotacoes = get_cotacao()

l_moedas = ['USD - Dólar', 'EUR - Euro', 'GBP - Libras']
l_valores = [1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]

opcao = 1
while opcao != 0:
    menu()
    opcao = int(input('Digite a opção.: '))
    match opcao:
        case 1: graficos_barra(l_moedas, l_valores)
        case 2: graficos_pizza(l_valores, l_moedas)
        case 3: graficos_dispersao(l_moedas, l_valores)
