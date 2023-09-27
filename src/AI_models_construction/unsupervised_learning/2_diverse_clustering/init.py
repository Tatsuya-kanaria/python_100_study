import pandas as pd
import numpy as np
from sklearn import cluster, preprocessing, mixture
from pyclustering.cluster.xmeans import xmeans
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer

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


# K-means
km = cluster.KMeans(n_clusters=3)
z_km = km.fit(X_norm)

# MeanShift
ms = cluster.MeanShift(seeds=X_norm)
ms.fit(X_norm)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
# print(cluster_centers)

# x_means
xm_c = kmeans_plusplus_initializer(X_norm, 2).initialize()
xm_i = xmeans(data=X_norm, initial_centers=xm_c, kmax=20, ccore=True)
xm_i.process()

z_xm = np.ones(X_norm.shape[0])
for k in range(len(xm_i._xmeans__clusters)):
    z_xm[xm_i._xmeans__clusters[k]] = k+1

# GMM
gmm = mixture.GaussianMixture(n_components=3, covariance_type="full")
z_gmm = gmm.fit(X_norm)
z_gmm = z_gmm.predict(X_norm)

# VBGMM
vbgmm = mixture.BayesianGaussianMixture(n_components=10, random_state=0)
vbgmm = vbgmm.fit(X_norm)
labels_vbgmm = vbgmm.predict(X_norm)

# MiniBatchKMeans
minikm = cluster.MiniBatchKMeans(n_clusters=3, batch_size=100)
z_minikm = minikm.fit(X_norm)
