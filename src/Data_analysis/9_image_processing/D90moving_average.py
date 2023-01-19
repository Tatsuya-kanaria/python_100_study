# %%
import numpy as np
import matplotlib.pyplot as plt

import D88graph_mov1 as D88
import D89graph_mov2 as D89


def moving_average(x, y):
    y_conv = np.convolve(y, np.ones(5)/float(5), mode='valid')
    x_dat = np.linspace(np.min(x), np.max(x), np.size(y_conv))
    return x_dat, y_conv


plt.plot(D88.list_df["time"], D88.list_df["people"], label="raw")
ma_x, ma_y = moving_average(D88.list_df["time"], D88.list_df["people"])
plt.plot(ma_x, ma_y, label="average")
plt.xlabel('time(sec.)')
plt.ylabel('population')
plt.ylim(0, 15)
plt.legend()
plt.show()

plt.plot(D89.list_df2["time"], D89.list_df2["people"], label="raw")
ma_x2, ma_y2 = moving_average(D89.list_df2["time"], D89.list_df2["people"])
plt.plot(ma_x2, ma_y2, label="average")
plt.xlabel('time(sec.)')
plt.ylabel('population')
plt.ylim(0, 15)
plt.legend()
plt.show()

plt.plot(ma_x, ma_y, label="1st")
plt.plot(ma_x2, ma_y2, label="2nd")
plt.xlabel('time(sec.)')
plt.ylabel('population')
plt.ylim(0, 15)
plt.legend()
plt.show()

# %%
