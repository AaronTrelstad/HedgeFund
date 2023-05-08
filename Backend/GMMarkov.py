from main import *

GM_Increase = {"Increase": 0, "Decrease": 0}
GM_Decrease = {"Increase": 0, "Decrease": 0}
for i in range(0, GM_len):
    GM[i][1] = float(GM[i][1])
    GM[i][2] = float(GM[i][2])
    volume = []
    for j in range(0, len(GM[i][3])):
        if GM[i][3][j] != ',':
            volume.append(GM[i][3][j])
    volume = "".join(volume)
    GM[i][3] = float(volume)
    GM[i][4] = float(GM[i][4])

for i in range(1, GM_len-1):
    if GM[i][4] <= 0:
        if GM[i+1][4] <= 0:
            GM_Decrease["Decrease"] += 1
        elif GM[i+1][4] > 0:
            GM_Decrease["Increase"] += 1
    elif GM[i][4] > 0:
        if GM[i+1][4] <= 0:
            GM_Increase["Decrease"] += 1
        elif GM[i+1][4] > 0:
            GM_Increase["Increase"] += 1

Increase_Total = GM_Increase["Increase"] + GM_Increase["Decrease"]
Decrease_Total = GM_Decrease["Increase"] + GM_Decrease["Decrease"]

GM_Increase['Increase'] = GM_Increase['Increase'] / Increase_Total
GM_Increase['Decrease'] = GM_Increase['Decrease'] / Increase_Total
GM_Decrease['Increase'] = GM_Decrease['Increase'] / Decrease_Total
GM_Decrease["Decrease"] = GM_Decrease['Decrease'] / Decrease_Total

print(GM_Increase)
print(GM_Decrease)