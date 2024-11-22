import requests
from .data_handler import add_data

def call_external_api():
    """

    :return:
    """
    try:
        api_key = "24U4897VFGCWKN64" #Не воруй #Not the best choice to use api that needs Api key and inclie it here without using ENV
        symbol = input("Input stock symbol: ")
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['Global Quote']
            add_data(f"Stock: {symbol}, Price: {data['05. price']}, Change: {data['09. change']}")
            print(f"Fetched price for {symbol}: {data['05. price']}, {'+' if float(data['09. change']) > 0 else '-'}{data['09. change']}")
            return True
        else:
            print(response.json())
            print("Symbol not found or API error.") #could print here response error of api isntead of this which gives no info  {response.json()}
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return "API Function failed due to an exception." # the function returns true and false in other 2 cases both booleans maybe instead of returning string here return false to keep consistent
