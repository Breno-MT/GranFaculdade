import requests

def get_cotacao(origem):
    url = f'https://api.exchangerate-api.com/v4/latest/{origem}'

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:
        return data["rates"]
    else:
        print('Erro ao buscar cotações: ', response.status_code)

def converter_cotacao(origem = 'USD', destino = 'BRL', valor = 1):
    rates = get_cotacao(destino)
    return round(valor / rates[origem], 2)

def menu():
    print()
    print('1 - Converter Dólar em Real')
    print('2 - Converter Euro em Real')
    print('3 - Converter Libras em Real')
    print('4 - Outra cotação')
    print('0 - Sair')
    print()

opcao = 1
while opcao != 0:
    menu()
    opcao = int(input('Digite a opção.: '))

    if(opcao):
        destino = 'BRL'
        valor = float(input('Digite o valor: '))

    match opcao:
        case 1: origem = 'USD'
        case 2: origem = 'EUR'
        case 3: origem = 'GBP'
        case 4:
            origem = input('Digite a origem: ')
            destino = input('Digite o destino: ')

    if (opcao):
        print()
        print(f'{origem} para {destino}:', converter_cotacao(origem, destino, valor))
