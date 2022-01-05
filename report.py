import matplotlib.pyplot as plt
import coingecko
import matplotlib.patheffects as path_effects

days = 7
bitcoin24Data = coingecko.getCoinData("bitcoin", days-1, "daily")
ethereum24Data = coingecko.getCoinData("ethereum", days-1, "daily")


# BTC
# list of prices
pricesBTC = []
for value in bitcoin24Data['prices']:
    pricesBTC.append(value[1])
# average price
averageBTC = sum(pricesBTC)/len(pricesBTC)
# list of volumes
volBTH = []
for value in bitcoin24Data['total_volumes']:
    volBTH.append(value[1])

# ETH
# list of prices
pricesETH = []
for value in ethereum24Data['prices']:
    pricesETH.append(value[1])
# average price
averageETH = sum(pricesETH)/len(pricesETH)
# list of only volumes
volETH = []
for value in ethereum24Data['total_volumes']:
    volETH.append(value[1])

# calculating RSI and other indexes

# BTC
RSIBTC = 0


# ETH
RSIETH = 0

index1 = plt.subplot(3,2,1)
yaxis = l = [i+1 for i in range(days)]
plt.plot(yaxis,pricesBTC,"-",color = 'y',label = "Bitcoin price")
plt.plot([1,days],[averageBTC,averageBTC],"--",color = 'g',label = "Average price")
plt.title("Bitcoin investment", size=18)

index2 = plt.subplot(3,2,2)
plt.plot(yaxis,pricesETH,"-",color = 'b',label = "Bitcoin price")
plt.plot([1,days],[averageETH,averageETH],"--",color = 'g',label = "Average price")
plt.title("Ethereum investment", size=18)


index3 = plt.subplot(3,2,5)
plt.bar(yaxis, volBTH, color='b', label="Bitcoin volume")
plt.title("This asset is volatile\n This asset is liquid\n Rsi Value: 70 \n sell this asset \n", size=13)

index4 = plt.subplot(3,2,6)
plt.bar(yaxis,volETH,color = 'b',label = "Bitcoin volume")
plt.title("This asset is volatile\n This asset is liquid\n Rsi Value: 70 \n sell this asset \n", size=13)

plt.show()

