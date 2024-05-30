import matplotlib
matplotlib.use("Agg")
from matplotlib.ticker import FormatStrFormatter

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")
data = pd.read_csv('Python.csv')
data = data.drop(data.index[[0]], axis = 0)

# Data Placeholder  
x = data['x']
one = data['one']
logn = data['logn']
nlogn = data['nlogn']
nsquare = data['nsquare']
n = data['n']   

# fig = plt.figure()
fig, ax = plt.subplots()
ax.set_title("O(n^2)")
fig.set_size_inches(9, 7)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

def animate(i):
    # ax.clear()
    plt.plot(x[:i], nsquare[:i], color="blue")
    if i > 25:
        ax.set_xlim(i - 25, i)
    else:
        ax.set_xlim(0, 25)

ani = FuncAnimation(fig, animate, blit=False, frames=100, interval=nsquare[1], repeat=False)    
plt.tight_layout()
ani.save(filename='O(n^2).gif',fps=30,dpi=300)
# plt.show()
plt.close('all')