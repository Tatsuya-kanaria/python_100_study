# %%
import pandas as pd
from sklearn import cluster, preprocessing, mixture
from pyclustering.cluster.xmeans import xmeans
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
import numpy as np
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

xm_c = kmeans_plusplus_initializer(X_norm, 2).initialize()
xm_i = xmeans(data=X_norm, initial_centers=xm_c, kmax=20, ccore=True)
xm_i.process()

km = cluster.KMeans(n_clusters=3)
z_km = km.fit(X_norm)

plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_km.labels_)
plt.scatter(z_km.cluster_centers_[:, 0], z_km.cluster_centers_[
            :, 1], s=250, marker="*", c="red")
plt.suptitle("K-means")
plt.show

gmm = mixture.GaussianMixture(n_components=3, covariance_type="full")
z_gmm = gmm.fit(X_norm)
z_gmm = z_gmm.predict(X_norm)

plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_gmm)
plt.suptitle("gmm")
plt.show

# %%
