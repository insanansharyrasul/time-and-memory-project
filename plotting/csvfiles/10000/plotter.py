import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")
data = pd.read_csv("Java.csv")
data = data.drop(data.index[[0]], axis=0)

fig = plt.figure(num=0, figsize=(12, 8))
ax1 = plt.subplot2grid((2, 6), (0, 0), colspan=2)
ax2 = plt.subplot2grid((2, 6), (0, 2), colspan=2)
ax3 = plt.subplot2grid((2, 6), (0, 4), colspan=2)
ax4 = plt.subplot2grid((2, 6), (1, 1), colspan=2)
ax5 = plt.subplot2grid((2, 6), (1, 3), colspan=2)

# Set Tile
ax1.set_title("O(1)")
ax2.set_title("O(log n)")
ax3.set_title("O(n)")
ax4.set_title("O(n log n)")
ax5.set_title("O(n^2)")
plt.suptitle("Java")

# Data Placeholder
x = data["x"]
one = data["one"]
logn = data["logn"]
n = data["n"]
nlogn = data["nlogn"]
nsquare = data["nsquare"]


def animate(i):
    ax1.plot(x[:i], one[:i], color="purple")
    ax2.plot(x[:i], logn[:i], color="orange")
    ax3.plot(x[:i], n[:i], color="teal")
    ax4.plot(x[:i], nlogn[:i], color="green")
    ax5.plot(x[:i], nsquare[:i], color="blue")
    if i > 25:
        ax1.set_xlim(i - 25, i)
        ax2.set_xlim(i - 25, i)
        ax3.set_xlim(i - 25, i)
        ax4.set_xlim(i - 25, i)
        ax5.set_xlim(i - 25, i)
    else:
        ax1.set_xlim(0, 25)
        ax2.set_xlim(0, 25)
        ax3.set_xlim(0, 25)
        ax4.set_xlim(0, 25)
        ax5.set_xlim(0, 25)


ani = FuncAnimation(fig, animate, blit=False, frames=100, interval=50, repeat=False)
plt.tight_layout()
ani.save(filename="Java.gif", fps=30, dpi=300)
# plt.show()
plt.close("all")
