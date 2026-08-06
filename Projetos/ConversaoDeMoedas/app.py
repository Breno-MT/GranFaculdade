import requests

def get_cotacao():
    url = 'https://api.exchangerate-api.com/v4/latest/BRL'

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:
        print(f"BRL ao USD: US$:{1 / data['rates']['USD']:.2f}")
        print(f"BRL ao EUR: EUR€:{1 / data['rates']['EUR']:.2f}")
    else:
        print('Erro ao buscar cotações: ', response.status_code)
    

get_cotacao()