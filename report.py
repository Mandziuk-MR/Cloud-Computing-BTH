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
volBTC = []
for value in bitcoin24Data['total_volumes']:
    volBTC.append(value[1])

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

#calculating RSI and other indexes
def RSIindex(prices):
    p = 0  # plus
    m = 0  # minus
    pc = 0  # pluscount
    mc = 0  # minuscout
    for record in range(len(prices)-1):
        change = float(prices[record]) - float(prices[record+1])
        if change > 0:
            p += change
            pc += 1
        elif change < 0:
            m -= change
            mc += 1
        if pc == 0:
            pc = 1
        if mc == 0:
            mc = 1
    a = p / pc
    b = m / mc
    if b == 0:
        b = 1
    rsi = 100 - 100 / (1 + a / b)
    return rsi

def Volatileindex(prices):
    X = 3 # 3% threshold for changes in price in that period
    maxl = float(max(prices))  # vlist= list of asset prices from last week
    minl = float(min(prices))
    value = ((maxl - minl) / maxl) * 100
    print(value)
    if value > X:
        return "This asset is volatile"
    else:
        return "This asset is not volatile"

def Liquidityindex(prices):
    pass
#we have only one price, so we can't check liquidity

def WhatToDo(RSI):
    if RSI <= 30:
        return "If you can, buy this asset"
    elif RSI >= 70:
        return "If you can, sell this asset"
    else:
        return "Keep this asset"

# creating plot

index1 = plt.subplot(3,2,1)
yaxis = [i+1 for i in range(days)]
plt.plot(yaxis,pricesBTC,"-",color = 'y',label = "Bitcoin price")
plt.plot([1,days],[averageBTC,averageBTC],"--",color = 'g',label = "Average price")
plt.title("Bitcoin investment", size=18)
plt.legend()
index1.tick_params(axis='both', which='major', labelsize=6)

index2 = plt.subplot(3,2,2)
plt.plot(yaxis,pricesETH,"-",color = 'm',label = "Ethereum price")
plt.plot([1,days],[averageETH,averageETH],"--",color = 'g',label = "Average price")
plt.title("Ethereum investment", size=18)
plt.legend()
index2.tick_params(axis='both', which='major', labelsize=6)

index3 = plt.subplot(3,2,5)
plt.bar(yaxis, volBTC, color='b', label="Bitcoin volume")
RSIBTC = RSIindex(pricesBTC)
plt.title(Volatileindex(pricesETH) + "\n RSI Value: % d \n" % RSIBTC + WhatToDo(RSIBTC) + "\n", size=13)
index3.tick_params(axis='both', which='major', labelsize=6)

index4 = plt.subplot(3,2,6)
plt.bar(yaxis,volETH,color = 'b',label = "Ethereum volume")
RSIETH = RSIindex(pricesETH)
plt.title(Volatileindex(pricesETH) + "\n RSI Value: % d \n" % RSIETH + WhatToDo(RSIETH) + "\n", size=13)
index4.tick_params(axis='both', which='major', labelsize=6)


plt.show()

