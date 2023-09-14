# %%
import pandas as pd
from sklearn import cluster, preprocessing
import matplotlib.pyplot as plt

df_wine_all = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df_wine = df_wine_all[[0, 10, 13]]
df_wine.columns = [u"class", u"color", u"proline"]
pd.DataFrame(df_wine)

X = df_wine[["color", "proline"]]
sc = preprocessing.StandardScaler()
X_norm = sc.fit_transform(X)
x = X_norm[:, 0]
y = X_norm[:, 1]
z = df_wine["class"]

plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z)
plt.show

km = cluster.KMeans(n_clusters=3)
z_km = km.fit(X_norm)
plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_km.labels_)
plt.scatter(z_km.cluster_centers_[:, 0], z_km.cluster_centers_[
            :, 1], s=250, marker="*", c="red")
plt.show

ms = cluster.MeanShift(seeds=X_norm)
ms.fit(X_norm)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
print(cluster_centers)

plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=labels)
plt.plot(cluster_centers[0, 0], cluster_centers[0, 1],
         marker="*", c="red", markersize=14)
plt.plot(cluster_centers[1, 0], cluster_centers[1, 1],
         marker="*", c="red", markersize=14)
plt.show

# %%
