# %%
import matplotlib.pyplot as plt

from init import x, y, z, z_km, labels, cluster_centers


# wine data visualization
plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z)
plt.show


# k-means
plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_km.labels_)
plt.scatter(z_km.cluster_centers_[:, 0], z_km.cluster_centers_[
            :, 1], s=250, marker="*", c="red")
plt.show

# MeanShift
plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=labels)
plt.plot(cluster_centers[0, 0], cluster_centers[0, 1],
         marker="*", c="red", markersize=14)
plt.plot(cluster_centers[1, 0], cluster_centers[1, 1],
         marker="*", c="red", markersize=14)
plt.show

# %%
