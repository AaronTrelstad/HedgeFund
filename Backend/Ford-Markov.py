from main import *

Increase = {"Increase": 0, "Decrease": 0}
Decrease = {"Increase": 0, "Decrease": 0}
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
            Decrease["Decrease"] += 1
        elif Ford[i+1][4] > 0:
            Decrease["Increase"] += 1
    elif Ford[i][4] > 0:
        if Ford[i+1][4] <= 0:
            Increase["Decrease"] += 1
        elif Ford[i+1][4] > 0:
            Increase["Increase"] += 1

Increase_Total = Increase["Increase"] + Increase["Decrease"]
Decrease_Total = Decrease["Increase"] + Decrease["Decrease"]

Increase['Increase'] = Increase['Increase'] / Increase_Total
Increase['Decrease'] = Increase['Decrease'] / Increase_Total
Decrease['Increase'] = Decrease['Increase'] / Decrease_Total
Decrease["Decrease"] = Decrease['Decrease'] / Decrease_Total



print(Increase)
print(Decrease)

