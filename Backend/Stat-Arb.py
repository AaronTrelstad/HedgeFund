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

"""
Look at data on comebacks meeting specifc 
criteria.
"""

##Only includes if greater
Ford_PartCome = {"Positive": [], "Negative": []}
GM_PartCome = {"Positive": [], "Negative": []}

for i in range(0, len(Ford)-1):
  change = []
  if Ford_PercentChange[i] > GM_PercentChange[i] and Ford_PercentChange[i] > 0:
    change.append(Ford_PercentChange[i]-GM_PercentChange[i])
    change.append(Ford_PercentChange[i+1]-GM_PercentChange[i+1])
    Ford_PartCome["Positive"].append(change)
  elif Ford_PercentChange[i] > GM_PercentChange[i] and Ford_PercentChange[i] < 0:
    change.append(Ford_PercentChange[i]-GM_PercentChange[i])
    change.append(Ford_PercentChange[i+1]-GM_PercentChange[i+1])
    Ford_PartCome["Negative"].append(change)
  elif Ford_PercentChange[i] < GM_PercentChange[i] and GM_PercentChange[i] > 0:
    change.append(GM_PercentChange[i]-Ford_PercentChange[i])
    change.append(GM_PercentChange[i+1]-Ford_PercentChange[i+1])
    GM_PartCome["Positive"].append(change)
  elif Ford_PercentChange[i] < GM_PercentChange[i] and GM_PercentChange[i] < 0:
    change.append(GM_PercentChange[i]-Ford_PercentChange[i])
    change.append(GM_PercentChange[i+1]-Ford_PercentChange[i+1])
    GM_PartCome["Negative"].append(change)

Ford_Positive = [0] * 3
for i in range(0, len(Ford_PartCome["Positive"])):
  Ford_Positive[0] += Ford_PartCome["Positive"][i][0]
  Ford_Positive[1] += Ford_PartCome["Positive"][i][1]
Ford_Positive[0] /= len(Ford_PartCome["Positive"])
Ford_Positive[1] /= len(Ford_PartCome["Positive"])

Ford_Negative = [0] * 3
for i in range(0, len(Ford_PartCome["Negative"])):
  Ford_Negative[0] += Ford_PartCome["Negative"][i][0]
  Ford_Negative[1] += Ford_PartCome["Negative"][i][1]
Ford_Negative[0] /= len(Ford_PartCome["Negative"])
Ford_Negative[1] /= len(Ford_PartCome["Negative"])

GM_Positive = [0] * 3
for i in range(0, len(GM_PartCome["Positive"])):
  GM_Positive[0] += GM_PartCome["Positive"][i][0]
  GM_Positive[1] += GM_PartCome["Positive"][i][1]
GM_Positive[0] /= len(GM_PartCome["Positive"])
GM_Positive[1] /= len(GM_PartCome["Positive"])

GM_Negative = [0] * 3
for i in range(0, len(GM_PartCome["Negative"])):
  GM_Negative[0] += GM_PartCome["Negative"][i][0]
  GM_Negative[1] += GM_PartCome["Negative"][i][1]
GM_Negative[0] /= len(GM_PartCome["Negative"])
GM_Negative[1] /= len(GM_PartCome["Negative"])




print(Ford_PartCome, GM_PartCome)
print(f"Ford: {Ford_Positive, Ford_Negative}")
print(f"GM: {GM_Positive, GM_Negative}")
print(F"Comebacks: {Ford_ComeAvg, GM_ComeAvg}")
print(f"Ford Markov: {Ford_Increase, Ford_Decrease}")
print(f"GM Markov: {GM_Increase, GM_Decrease}")


'''
This shows that if Ford is less than there is 
a better chance of it going positive opposed to GM
'''

'''
Buy a stock when under and sell when over
Initially start with 100 shares 
Buy and Sell use 10 shares
'''
Ford_Shares = 0
GM_Shares = 0

money = 1000
initial = money

GM_Moves = []
Ford_Moves = []

shares = 20

for i in range(0, len(Ford)):
  differ = abs(Ford_PercentChange[i] - GM_PercentChange[i])
  ##Anytime Ford is lower it is better to buy
  if Ford_PercentChange[i] > GM_PercentChange[i] and differ > diff_avg:
    if Ford_Shares >= shares:
      Ford_Shares -= shares
      money += Ford_Close[i] * shares
      Ford_Action = "Sell"
      Ford_Moves.append(Ford_Action)
    if money > GM_Close[i] * shares:
      money -= GM_Close[i] * shares
      GM_Shares += shares
      GM_Action = "Buy"
      GM_Moves.append(GM_Action)
  elif Ford_PercentChange[i] < GM_PercentChange[i] and differ > diff_avg:
    if GM_Shares >= shares:
      GM_Shares -= shares
      money += GM_Close[i] * shares
      GM_Action = "Sell"
      GM_Moves.append(GM_Action)
    if money > Ford_Close[i] * shares:
      money -= Ford_Close[i] * shares
      Ford_Shares += shares
      Ford_Action = "Buy"
      Ford_Moves.append(Ford_Action)

print(f"GM: {GM_Moves}, Ford: {Ford_Moves}")
print(money, Ford_Shares, GM_Shares)
added = (Ford_Shares * Ford_Close[-1]) + (GM_Shares * GM_Close[-1])
total = money + added
returns = ((total - initial) / initial) * 100
print(f"{round(returns, 2)}%, ${total}")









