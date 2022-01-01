import requests

BASE_URL = "https://api.coingecko.com/api/v3"
CURRENCY = "usd"

# coin = string, name of the coin e.g. bitcoin
# days = number, get data up to number of days ago
# interval = string, minutely/hourly/daily
# returns dictionary of prices, market caps and total volumes
def getCoinData(coin, days, interval = "daily"):
    payload = {'id': coin, 'vs_currency': CURRENCY, 'days': days, 'interval': interval}
    response = requests.get(BASE_URL + "/coins/" + coin + "/market_chart", params = payload)

    return response.json()