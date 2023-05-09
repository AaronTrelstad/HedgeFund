import csv
from StatArb import diff_avg

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

Ford_Shares = 0
GM_Shares = 0

money = 1000
initial = money

GM_Moves = []
Ford_Moves = []

investment_small = 100
investment_big = 120


differ = abs(CurrFord[0][2] - CurrGM[0][2])
  ##Anytime Ford is lower it is better to buy
if CurrFord[0][2] > CurrGM[0][2] and differ > diff_avg:
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

print(Ford_Moves, GM_Moves)
print(f"Money: ${money, initial}")