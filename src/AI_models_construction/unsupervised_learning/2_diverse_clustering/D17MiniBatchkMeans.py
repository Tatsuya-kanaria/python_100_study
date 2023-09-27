# %%
import matplotlib.pyplot as plt

from init import x, y, z_km, z_minikm

plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_km.labels_)
plt.scatter(z_km.cluster_centers_[:, 0], z_km.cluster_centers_[
            :, 1], s=250, marker="*", c="red")
plt.suptitle("k-means")
plt.show

# minibatch kmeans
plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_minikm.labels_)
plt.scatter(z_minikm.cluster_centers_[:, 0], z_minikm.cluster_centers_[
            :, 1], s=250, marker="*", c="red")
plt.suptitle("mini-k-means")
plt.show

# %%
