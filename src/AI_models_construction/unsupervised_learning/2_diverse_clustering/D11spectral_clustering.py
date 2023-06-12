# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster, preprocessing
from sklearn import datasets
from IPython.display import display


X, z = datasets.make_moons(n_samples=200, noise=0.05, random_state=0)
sc = preprocessing.StandardScaler()
X_norm = sc.fit_transform(X)
display(X_norm)

x = X_norm[:, 0]
y = X_norm[:, 1]

plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z)
plt.show

# k-means
km = cluster.KMeans(n_clusters=2)
z_km = km.fit(X_norm)

plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_km.labels_)
plt.scatter(z_km.cluster_centers_[:, 0], z_km.cluster_centers_[
            :, 1], s=250, marker="*", c="red")
plt.suptitle("k-means")
plt.show

# SpectralClustering

spc = cluster.SpectralClustering(n_clusters=2, affinity="nearest_neighbors")
z_spc = spc.fit(X_norm)

plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_spc.labels_)
plt.suptitle("Spectral Clustering")
plt.show

# %%
