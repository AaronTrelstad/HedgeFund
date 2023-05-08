from main import *
import matplotlib.pyplot as plt
from scipy import stats

x = []
for idx, num in enumerate(Ford):
  x.append(idx + 1)

days = 30

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
plt.plot(x[-days:], Ford_model)
plt.plot(x[-days:], GM_model)

plt.savefig("percentChange.png")