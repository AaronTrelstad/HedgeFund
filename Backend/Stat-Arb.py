from main import *
import matplotlib.pyplot as plt
from scipy import stats

x = []
for idx, num in enumerate(Ford):
  x.append(idx + 1)

days = 30

slope, intercept, r, p, std_err = stats.linregress(x[-days:], Ford[-days:])

def linear(x):
  return slope * x + intercept

mymodel = list(map(linear, x[-days:]))

plt.scatter(x[-days:], Ford[-days:])
plt.plot(x[-days:], mymodel)
plt.savefig("percentChange30.png")