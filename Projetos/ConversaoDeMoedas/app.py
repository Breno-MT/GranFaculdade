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

print(converter_cotacao())
