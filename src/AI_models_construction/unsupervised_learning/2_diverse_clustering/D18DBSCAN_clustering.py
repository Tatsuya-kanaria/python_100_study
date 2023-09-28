# %%
import matplotlib.pyplot as plt
from sklearn import datasets, preprocessing, cluster

X = datasets.make_blobs(n_samples=1000, random_state=10,
                        centers=5, cluster_std=1.2)[0]
sc = preprocessing.StandardScaler()
X_norm = sc.fit_transform(X)
x = X_norm[:, 0]
y = X_norm[:, 1]

plt.figure(figsize=(10, 3))
plt.scatter(x, y)
plt.suptitle("blob")
plt.show

X_moon = datasets.make_moons(n_samples=1000, noise=0.05, random_state=0)[0]
sc = preprocessing.StandardScaler()
X_moon_norm = sc.fit_transform(X_moon)
x_moon = X_moon_norm[:, 0]
y_moon = X_moon_norm[:, 1]

plt.figure(figsize=(10, 3))
plt.scatter(x_moon, y_moon)
plt.suptitle("moon")
plt.show

km_moon = cluster.KMeans(n_clusters=2)
z_km_moon = km_moon.fit(X_moon_norm)
plt.figure(figsize=(10, 3))
plt.scatter(x_moon, y_moon, c=z_km_moon.labels_)
plt.scatter(z_km_moon.cluster_centers_[:, 0], z_km_moon.cluster_centers_[
            :, 1], s=250, marker="*", c="red")
plt.suptitle("k-means")
plt.show

dbscan = cluster.DBSCAN(eps=0.2, min_samples=5, metric="euclidean")
labels = dbscan.fit_predict(X_moon_norm)
plt.figure(figsize=(10, 3))
plt.scatter(x_moon, y_moon, c=labels)
plt.suptitle("dbscan")
plt.show

km = cluster.KMeans(n_clusters=5)
z_km = km.fit(X_norm)
plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_km.labels_)
plt.scatter(z_km.cluster_centers_[:, 0], z_km.cluster_centers_[
            :, 1], s=250, marker="*", c="red")
plt.suptitle("k_means")

dbscan = cluster.DBSCAN(eps=0.2, min_samples=5, metric="euclidean")
labels = dbscan.fit_predict(X_norm)
plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=labels)
plt.suptitle("dbscan")
plt.show

# %%
