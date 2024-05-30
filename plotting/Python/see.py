import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")

def animate(i):
    data = pd.read_csv("nsquare.csv")
    x = data['n']
    y1 = data['times']

    plt.cla()

    plt.plot(x, y1, label="n^2")
    plt.tight_layout

ani = FuncAnimation(plt.gcf(), animate)

plt.tight_layout()
plt.show()
