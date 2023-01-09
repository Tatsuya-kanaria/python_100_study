# %%
import numpy as np
import matplotlib.pyplot as plt

import D71network_visualization as D71
import D74membership_change_over_time as D74


T_NUM = 36
NUM = len(D71.df_links.index)
NUM_PhaseDiagram = 20
phaseDiagram = np.zeros((NUM_PhaseDiagram, NUM_PhaseDiagram))
for i_p in range(NUM_PhaseDiagram):
    for i_d in range(NUM_PhaseDiagram):
        percent_percolation = 0.05 * i_p
        percent_disapparence = 0.05 * i_d
        list_active = np.zeros(NUM)
        list_active[0] = 1
        for _ in range(T_NUM):
            list_active = D74.simulate_population(
                NUM, list_active, percent_percolation, percent_disapparence, D71.df_links)
        phaseDiagram[i_p][i_d] = sum(list_active)

plt.matshow(phaseDiagram)
plt.colorbar(shrink=0.8)
plt.xlabel('percent_disapparence')
plt.ylabel('percent_percolation')
plt.xticks(np.arange(0.0, 20.0, 5), np.arange(0.0, 1.0, 0.25))
plt.yticks(np.arange(0.0, 20.0, 5), np.arange(0.0, 1.0, 0.25))
plt.tick_params(bottom=False, left=False, right=False, top=False)
plt.show()

# %%
