import apikey 
import requests

def get_cryptocurrency_info(crypto_name):
    headers = {
        'X-CMC_PRO_API_KEY' : apikey.key,
        'Accept' : 'application/json'
    }

    params = {
        'start' : '1',
        'limit' : '10',
        'convert' : 'GBP'
    }

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    for coin in data['data']:
        if coin['name'].lower() == crypto_name.lower():
            return coin

    return None

def main():
    crypto_name = input("Enter the name of a cryptocurrency: ")
    crypto_info = get_cryptocurrency_info(crypto_name)
    if crypto_info:
        print(f"Symbol: {crypto_info['symbol']}")
        print(f"Price (GBP): {crypto_info['quote']['GBP']['price']}")
    else:
        print("Cryptocurrency not found.")

if __name__ == "__main__":
    main()
