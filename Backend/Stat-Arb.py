from main import *
import matplotlib.pyplot as plt
from scipy import stats

x = []
for idx, num in enumerate(Ford):
  x.append(idx + 1)

days = 30

##Initially we will use just closing prices
Ford_Close = []
GM_Close = []
for i in range(0, len(Ford)):
  Ford_Close.append(float(Ford[i][2]))
  GM_Close.append(float(GM[i][2]))

Ford_PercentChange = []
GM_PercentChange = []
for i in range(0, len(Ford)):
  Ford_PercentChange.append(float(Ford[i][4]))
  GM_PercentChange.append(float(GM[i][4]))


Ford_slope, Ford_intercept, Ford_r, Ford_p, Ford_std_err = stats.linregress(x[-days:], Ford_PercentChange[-days:])
GM_slope, GM_intercept, GM_r, GM_p, GM_std_err = stats.linregress(x[-days:], GM_PercentChange[-days:])

def Ford_linear(x):
  return Ford_slope * x + Ford_intercept

def GM_linear(x):
  return GM_slope * x + GM_intercept

Ford_model = list(map(Ford_linear, x[-days:]))
GM_model = list(map(GM_linear, x[-days:]))

plt.scatter(x[-days:], Ford_PercentChange[-days:])
plt.scatter(x[-days:], GM_PercentChange[-days:])
plt.plot(x[-days:], Ford_PercentChange[-days:])
plt.plot(x[-days:], GM_PercentChange[-days:])
plt.savefig("percentChange.png")

##Short the stock that is over 
##Long the stock that is under

'''
Buy a stock when under and sell when over
Initially start with 100 shares 
Buy and Sell use 10 shares
'''
Ford_Shares = 100
GM_Shares = 100

Ford_Money = Ford_Shares * Ford_Close[0]
GM_Money = GM_Shares * GM_Close[0]

Ford_Initial = Ford_Money
GM_Initial = GM_Money

print(Ford_Money, GM_Money)

GM_Moves = []
Ford_Moves = []

for i in range(0, len(Ford)):
  if Ford_PercentChange[i] > GM_PercentChange[i] and Ford_PercentChange[i] < 0:
    GM_Action = "Buy"
    GM_Shares += 10
    GM_Money -= GM_Close[i] * 10
    GM_Moves.append(GM_Action)
    
  elif Ford_PercentChange[i] < GM_PercentChange[i] and GM_PercentChange[i] < 0:
    Ford_Action = "Buy"
    Ford_Shares += 10
    Ford_Money -= Ford_Close[i] * 10
    Ford_Moves.append(Ford_Action)

  elif Ford_PercentChange[i] > GM_PercentChange[i] and GM_PercentChange[i] > 0:
    Ford_Action = "Sell"
    Ford_Shares -= 10
    Ford_Money += Ford_Close[i] * 10
    Ford_Moves.append(Ford_Action)

  elif Ford_PercentChange[i] < GM_PercentChange[i] and Ford_PercentChange[i] > 0:
    GM_Action = "Sell"
    GM_Shares -= 10
    GM_Money += GM_Close[i] * 10
    GM_Moves.append(GM_Action)

print(GM_Moves, Ford_Moves)
Ford_Money += Ford_Shares * Ford_Close[-1]
GM_Money += GM_Shares * GM_Close[-1]
Ford_Returns = ((Ford_Money-Ford_Initial)/Ford_Initial) * 100
GM_Returns = ((GM_Money-GM_Initial)/GM_Initial) * 100
print(Ford_Returns, GM_Returns)


