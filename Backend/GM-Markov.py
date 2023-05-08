from main import *

Increase = {"Increase": 0, "Decrease": 0}
Decrease = {"Increase": 0, "Decrease": 0}
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
            Decrease["Decrease"] += 1
        elif GM[i+1][4] > 0:
            Decrease["Increase"] += 1
    elif GM[i][4] > 0:
        if GM[i+1][4] <= 0:
            Increase["Decrease"] += 1
        elif GM[i+1][4] > 0:
            Increase["Increase"] += 1

Increase_Total = Increase["Increase"] + Increase["Decrease"]
Decrease_Total = Decrease["Increase"] + Decrease["Decrease"]

Increase['Increase'] = Increase['Increase'] / Increase_Total
Increase['Decrease'] = Increase['Decrease'] / Increase_Total
Decrease['Increase'] = Decrease['Increase'] / Decrease_Total
Decrease["Decrease"] = Decrease['Decrease'] / Decrease_Total

print(Increase)
print(Decrease)