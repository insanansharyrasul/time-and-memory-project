import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_values']
    y1 = data['times1']
    y2 = data['times2']
    y3 = data['times3']
    y4 = data['times4']
    y5 = data['times5']

    plt.cla()

    # plt.plot(x, y1, label='O(1)')
    # plt.plot(x, y2, label='O(log n)')
    # plt.plot(x, y3, label='O(n)')
    # plt.plot(x, y4, label='O(n log n)')
    plt.plot(x, y5, label='O(n^2)')
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=0)

plt.tight_layout()
# plt.autoscale()
plt.show()

