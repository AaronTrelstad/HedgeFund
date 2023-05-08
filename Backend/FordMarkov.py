from main import *

Ford_Increase = {"Increase": 0, "Decrease": 0}
Ford_Decrease = {"Increase": 0, "Decrease": 0}
for i in range(0, Ford_len):
    Ford[i][1] = float(Ford[i][1])
    Ford[i][2] = float(Ford[i][2])
    volume = []
    for j in range(0, len(Ford[i][3])):
        if Ford[i][3][j] != ',':
            volume.append(Ford[i][3][j])
    volume = "".join(volume)
    Ford[i][3] = float(volume)
    Ford[i][4] = float(Ford[i][4])

for i in range(1, Ford_len-1):
    if Ford[i][4] <= 0:
        if Ford[i+1][4] <= 0:
            Ford_Decrease["Decrease"] += 1
        elif Ford[i+1][4] > 0:
            Ford_Decrease["Increase"] += 1
    elif Ford[i][4] > 0:
        if Ford[i+1][4] <= 0:
            Ford_Increase["Decrease"] += 1
        elif Ford[i+1][4] > 0:
            Ford_Increase["Increase"] += 1

Increase_Total = Ford_Increase["Increase"] + Ford_Increase["Decrease"]
Decrease_Total = Ford_Decrease["Increase"] + Ford_Decrease["Decrease"]

Ford_Increase['Increase'] = Ford_Increase['Increase'] / Increase_Total
Ford_Increase['Decrease'] = Ford_Increase['Decrease'] / Increase_Total
Ford_Decrease['Increase'] = Ford_Decrease['Increase'] / Decrease_Total
Ford_Decrease["Decrease"] = Ford_Decrease['Decrease'] / Decrease_Total



print(Ford_Increase)
print(Ford_Decrease)

