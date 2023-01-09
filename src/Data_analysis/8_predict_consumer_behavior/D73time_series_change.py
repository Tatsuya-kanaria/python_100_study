# %%
import matplotlib.pyplot as plt

import D72information_propagation as D72


list_timeSeries_num = []
for i in range(len(D72.list_timeSeries)):
    list_timeSeries_num.append(sum(D72.list_timeSeries[i]))

plt.plot(list_timeSeries_num)
plt.show()

# %%
