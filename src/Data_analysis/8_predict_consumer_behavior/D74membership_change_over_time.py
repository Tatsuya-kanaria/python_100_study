# %%
import numpy as np
import matplotlib.pyplot as plt

import D71network_visualization as D71
import D72information_propagation as D72


def simulate_population(num, list_active, percent_percolation, percent_disapparence, df_links):
    # 拡散
    for i in range(num):
        if list_active[i] == 1:
            for j in range(num):
                if df_links.iloc[i][j] == 1:
                    if D72.determine_link(percent_percolation) == 1:
                        list_active[j] = 1

    # 消滅
    for i in range(num):
        if D72.determine_link(percent_disapparence) == 1:
            list_active[i] = 0
    return list_active


percent_percolation = 0.1
percent_disapparence = 0.05
T_NUM = 100
NUM = len(D71.df_links.index)
list_active = np.zeros(NUM)
list_active[0] = 1

list_timeSeries = []

for _ in range(T_NUM):
    list_active = simulate_population(
        NUM, list_active, percent_percolation, percent_disapparence, D71.df_links)
    list_timeSeries.append(list_active.copy())

if __name__ == '__main__':
    # 時系列グラフを描く
    list_timeSeries_num = []
    for i in range(len(list_timeSeries)):
        list_timeSeries_num.append(sum(list_timeSeries[i]))

    plt.plot(list_timeSeries_num)
    plt.show()

    percent_disapparence = 0.2
    list_active = np.zeros(NUM)
    list_active[0] = 1
    list_timeSeries = []
    for _ in range(T_NUM):
        list_active = simulate_population(
            NUM, list_active, percent_percolation, percent_disapparence, D71.df_links)
        list_timeSeries.append(list_active.copy())

    list_timeSeries_num = []
    for i in range(len(list_timeSeries)):
        list_timeSeries_num.append(sum(list_timeSeries[i]))

    plt.plot(list_timeSeries_num)
    plt.show()

# %%
