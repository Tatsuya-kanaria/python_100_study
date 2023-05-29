# %%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.metrics import silhouette_samples

from D4search_for_optimal_class import X, z_km


cluster_labels = np.unique(z_km.labels_)
n_clusters = cluster_labels.shape[0]
silhouette_vals = silhouette_samples(X, z_km.labels_)

y_ax_lower, y_ax_upper = 0, 0
yticks = []
fig = plt.figure(figsize=(10, 3))
ax4 = fig.add_subplot(1, 1, 1)

for i, c in enumerate(cluster_labels):
    c_silhouette_vals = silhouette_vals[z_km.labels_ == c]
    print(len(c_silhouette_vals))
    c_silhouette_vals.sort()
    y_ax_upper += len(c_silhouette_vals)
    color = cm.jet(float(i)/n_clusters)
    ax4.barh(
        range(y_ax_lower, y_ax_upper),
        c_silhouette_vals,
        height=1.0,
        edgecolor="none",
        color=color
    )
    yticks.append((y_ax_lower+y_ax_upper) / 2.)
    y_ax_lower += len(c_silhouette_vals)

silhouette_avg = np.mean(silhouette_vals)

ax4.axvline(silhouette_avg, color="red", linestyle="--")
plt.ylabel("Cluster")
plt.xlabel("Silhouette Coefficient")
plt.yticks(yticks, cluster_labels + 1)

# %%
