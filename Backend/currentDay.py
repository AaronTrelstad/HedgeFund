import csv
from StatArb import diff_avg

"""
Calculates signal for a specific day
"""

with open('currentFord.csv') as f:
  reader = csv.reader(f)
  CurrFord = list(reader)

with open('currentGM.csv') as f:
  reader = csv.reader(f)
  CurrGM = list(reader)

CurrFord_key = CurrFord[0]
CurrGM_key = CurrGM[0]
CurrFord = CurrFord[1:]
CurrGM = CurrGM[1:]

print(CurrFord, CurrGM)

CurrFord[0][1] = float(CurrFord[0][1])
CurrFord[0][2] = float(CurrFord[0][2])
CurrGM[0][1] = float(CurrGM[0][1])
CurrGM[0][2] = float(CurrGM[0][2])

###Paste in theb current number of shares
Ford_Shares = 34.75320639953611
GM_Shares = 18.40977713223365

"""
$200 is a full confidence buy/sell, I need to create a way to 
price the other buy/sells
"""

money = 0
initial = money

GM_Moves = []
Ford_Moves = []

investment_small = 200
investment_big = 200

differ = abs(CurrFord[0][2] - CurrGM[0][2])
  ##Anytime Ford is lower it is better to buy
if CurrFord[0][2] > CurrGM[0][2]:
    if Ford_Shares >= investment_small/CurrFord[0][1]:
        Ford_Shares -= investment_small/CurrFord[0][1]
        money += investment_small
        Ford_Action = "Sell"
        Ford_Moves.append(Ford_Action)
    if money >= investment_small:
        money -= investment_small
        GM_Shares += investment_small/CurrGM[0][1]
        GM_Action = "Buy"
        GM_Moves.append(GM_Action)
elif CurrFord[0][2] < CurrGM[0][2]:
    if GM_Shares >= investment_big/CurrGM[0][1]:
        GM_Shares -= investment_big/CurrGM[0][1]
        money += investment_big
        GM_Action = "Sell"
        GM_Moves.append(GM_Action)
    if money >= investment_big:
        money -= investment_big
        Ford_Shares += investment_big/CurrFord[0][1]
        Ford_Action = "Buy"
        Ford_Moves.append(Ford_Action)
 
print(f"Ford: {Ford_Moves}, GM: {GM_Moves}")
print(f"Ford Shares: {Ford_Shares}, GM Shares: {GM_Shares}")
print(f"Money: ${money, initial}")
