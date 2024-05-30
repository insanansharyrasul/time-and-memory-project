import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

name = 'n.csv'
data = pd.read_csv(name)
x = data['n']
y = data['times']
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
plt.title(name)
plt.scatter(x, y)
plt.plot(x, p(x), color="red")
plt.show()