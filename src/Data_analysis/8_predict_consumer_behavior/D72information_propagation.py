# %%
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

import D71network_visualization as D71


def determine_link(percent):
    rand_val = np.random.rand()
    if rand_val <= percent:
        return 1
    else:
        return 0


def simulate_percolation(num, list_active, percent_percolation):
    for i in range(num):
        if list_active[i] == 1:
            for j in range(num):
                node_name = "Node" + str(j)
                if D71.df_links[node_name].iloc[i] == 1:
                    if determine_link(percent_percolation) == 1:
                        list_active[j] = 1
    return list_active


percent_percolation = 0.1
T_NUM = 100
NUM = len(D71.df_links.index)
list_active = np.zeros(NUM)
list_active[0] = 1
list_timeSeries = []
for _ in range(T_NUM):
    list_active = simulate_percolation(NUM, list_active, percent_percolation)
    list_timeSeries.append(list_active.copy())


def active_node_coloring(list_active):
    # print(list_timeSeries[t])
    list_color = []
    for i in range(len(list_timeSeries[t])):
        if list_timeSeries[t][i] == 1:
            list_color.append("r")
        else:
            list_color.append("k")
    # print(len(list_color))
    return list_color


t = 0
nx.draw_networkx(D71.G, font_color="w",
                 node_color=active_node_coloring(list_timeSeries[t]))
plt.show()

t = 10
nx.draw_networkx(D71.G, font_color="w",
                 node_color=active_node_coloring(list_timeSeries[t]))
plt.show()

t = 99
nx.draw_networkx(D71.G, font_color="w",
                 node_color=active_node_coloring(list_timeSeries[t]))
plt.show()

# %%
