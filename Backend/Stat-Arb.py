from main import *
from FordMarkov import *
from GMMarkov import *
import matplotlib.pyplot as plt
from scipy import stats

x = []
for idx, num in enumerate(Ford):
  x.append(idx + 1)

days = len(Ford)

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
Need a way to calculate correlation so that simulation only
runs in ideal situations
'''

##Gives percent differene of slopes
difference = abs(GM_slope - Ford_slope) / GM_slope

diff = []
for i in range(0, len(Ford_PercentChange)):
  diff.append(abs(Ford_PercentChange[i]-GM_PercentChange[i]))

diff_avg = sum(diff) / len(diff)

print(diff_avg)



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

print(f"Ford: ${Ford_Money}, GM: ${GM_Money}")

"""
How many stocks we buy/sell will be 
determined by the Markov Chain propabilities
"""

Ford_Comeback = []
GM_Comeback = []

for i in range(0, len(Ford)-1):
  change = []
  if Ford_PercentChange[i] < GM_PercentChange[i]:
    change.append(Ford_PercentChange[i]-GM_PercentChange[i])
    change.append(Ford_PercentChange[i+1]-GM_PercentChange[i+1])
    Ford_Comeback.append(change)
  elif Ford_PercentChange[i] > GM_PercentChange[i]:
    change.append(GM_PercentChange[i]-Ford_PercentChange[i])
    change.append(GM_PercentChange[i+1]-Ford_PercentChange[i+1])
    GM_Comeback.append(change)

Ford_ComeAvg = [0] * 2
GM_ComeAvg = [0] * 2

for i in range(0, len(Ford_Comeback)):
  Ford_ComeAvg[0] += Ford_Comeback[i][0]
  Ford_ComeAvg[1] += Ford_Comeback[i][1]
  GM_ComeAvg[0] += GM_Comeback[i][0]
  GM_ComeAvg[1] += GM_Comeback[i][1]

Ford_ComeAvg[0] /= len(Ford_Comeback)
Ford_ComeAvg[1] /= len(Ford_Comeback)
GM_ComeAvg[0] /= len(GM_Comeback)
GM_ComeAvg[1] /= len(GM_Comeback)

print(F"Comebacks: {Ford_ComeAvg, GM_ComeAvg}")

Ford_Drawback = []
GM_Drawback = []

for i in range(0, len(Ford)-1):
  change = []
  if Ford_PercentChange[i] > GM_PercentChange[i]:
    change.append(Ford_PercentChange[i]-GM_PercentChange[i])
    change.append(Ford_PercentChange[i+1]-GM_PercentChange[i+1])
    Ford_Drawback.append(change)
  elif Ford_PercentChange[i] < GM_PercentChange[i]:
    change.append(GM_PercentChange[i]-Ford_PercentChange[i])
    change.append(GM_PercentChange[i+1]-Ford_PercentChange[i+1])
    GM_Drawback.append(change)

Ford_DrawAvg = [0] * 2
GM_DrawAvg = [0] * 2

for i in range(0, len(Ford_Drawback)):
  Ford_DrawAvg[0] += Ford_Drawback[i][0]
  Ford_DrawAvg[1] += Ford_Drawback[i][1]
  GM_DrawAvg[0] += GM_Drawback[i][0]
  GM_DrawAvg[1] += GM_Drawback[i][1]

Ford_DrawAvg[0] /= len(Ford_Drawback)
Ford_DrawAvg[1] /= len(Ford_Drawback)
GM_DrawAvg[0] /= len(GM_Drawback)
GM_DrawAvg[1] /= len(GM_Drawback)

print(f"Drawback: {Ford_DrawAvg, GM_DrawAvg}")

'''
This shows that if Ford is less than there is 
a better chance of it going positive opposed to GM
'''



GM_Moves = []
Ford_Moves = []

for i in range(0, len(Ford)):
  differ = abs(Ford_PercentChange[i] - GM_PercentChange[i])
  if Ford_PercentChange[i] > GM_PercentChange[i] and Ford_PercentChange[i] < 0 and differ > diff_avg:
    GM_Action = "Buy"
    GM_Shares += 10
    GM_Money -= GM_Close[i] * 10
    GM_Moves.append(GM_Action)
    
  elif Ford_PercentChange[i] < GM_PercentChange[i] and GM_PercentChange[i] < 0 and differ > diff_avg:
    Ford_Action = "Buy"
    Ford_Shares += 10
    Ford_Money -= Ford_Close[i] * 10
    Ford_Moves.append(Ford_Action)

  elif Ford_PercentChange[i] > GM_PercentChange[i] and GM_PercentChange[i] > 0 and differ > diff_avg:
    Ford_Action = "Sell"
    Ford_Shares -= 10
    Ford_Money += Ford_Close[i] * 10
    Ford_Moves.append(Ford_Action)

  elif Ford_PercentChange[i] < GM_PercentChange[i] and Ford_PercentChange[i] > 0 and differ > diff_avg:
    GM_Action = "Sell"
    GM_Shares -= 10
    GM_Money += GM_Close[i] * 10
    GM_Moves.append(GM_Action)

print(GM_Moves, Ford_Moves)
Ford_Money += Ford_Shares * Ford_Close[-1]
GM_Money += GM_Shares * GM_Close[-1]
Ford_Returns = ((Ford_Money-Ford_Initial)/Ford_Initial) * 100
GM_Returns = ((GM_Money-GM_Initial)/GM_Initial) * 100
print(F"{Ford_Returns}%, Ford: ${Ford_Money}, {GM_Returns}%, GM: ${GM_Money}")









