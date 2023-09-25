# %%
import matplotlib.pyplot as plt

from init import x, y, z_km, z_gmm


plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_km.labels_)
plt.scatter(z_km.cluster_centers_[:, 0], z_km.cluster_centers_[
            :, 1], s=250, marker="*", c="red")
plt.suptitle("K-means")
plt.show

# GMM
plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_gmm)
plt.suptitle("gmm")
plt.show

# %%
