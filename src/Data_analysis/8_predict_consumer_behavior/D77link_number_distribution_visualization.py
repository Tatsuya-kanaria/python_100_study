# %%
import numpy as np
import matplotlib.pyplot as plt

import D76real_data as D76

NUM = len(D76.df_mem_links.index)
array_linkNum = np.zeros(NUM)
for i in range(NUM):
    array_linkNum[i] = sum(D76.df_mem_links["Node" + str(i)])

plt.hist(array_linkNum, bins=10, range=(0, 250))
plt.show()

# %%
