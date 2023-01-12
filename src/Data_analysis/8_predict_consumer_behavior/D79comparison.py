# %%
import numpy as np
import matplotlib.pyplot as plt

import D74membership_change_over_time as D74
import D76real_data as D76

percent_percolation = 0.025759421962846578
percent_disapparence = 0.10147163541419416

# D80 は T_NUM を36ヶ月にしてしゅミュレートする
T_NUM = 36
NUM = len(D76.df_mem_links.index)
list_active = np.zeros(NUM)
list_active[0] = 1
list_timeSeries = []
for t in range(T_NUM):
    list_active = D74.simulate_population(
        NUM, list_active, percent_percolation, percent_disapparence, D76.df_mem_links)
    list_timeSeries.append(list_active.copy())

list_timeSeries_num = []
for i in range(len(list_timeSeries)):
    list_timeSeries_num.append(sum(list_timeSeries[i]))

T_NUM = len(D76.df_mem_info.columns) - 1
list_timeSeries_num_real = []
for t in range(0, T_NUM):
    list_timeSeries_num_real.append(
        len(D76.df_mem_info[D76.df_mem_info[str(t)] == 1].index))

plt.plot(list_timeSeries_num, label="simulated")
plt.plot(list_timeSeries_num_real, label="real")
plt.xlabel('month')
plt.ylabel('population')
plt.legend(loc="lower right")
plt.show

# %%
