# %%
from scipy.cluster.hierarchy import dendrogram, fcluster
import matplotlib.pyplot as plt

from D6hierarchical_clustering import Z


fig2, ax2 = plt.subplots(figsize=(20, 5))
ax2 = dendrogram(Z)
fig2.show()

# clusters = fcluster(Z, t=3, criterion="maxclust")
# for i, c in enumerate(clusters):
# print(i, c)

clusters_disdance = fcluster(Z, t=1.6, criterion="distance")
for i, c in enumerate(clusters_disdance):
    print(i, c)


# %%
