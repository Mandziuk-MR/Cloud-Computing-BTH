import coingecko

def lambda_handler(event, context):
    bitcoin24Data = coingecko.getCoinData("bitcoin", 1, "hourly")
    print("Prices: ")
    print(bitcoin24Data['prices'])
    print("Total volumes: ")
    print(bitcoin24Data['total_volumes'])