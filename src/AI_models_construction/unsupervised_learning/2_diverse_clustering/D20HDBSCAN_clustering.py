# %%
from sklearn import datasets, cluster
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
import hdbscan
import seaborn as sns


centers = [[1, 0.5], [2, 2], [1, -1]]
stds = [0.1, 0.4, 0.2]

X = datasets.make_blobs(n_samples=1000, centers=centers,
                        cluster_std=stds, random_state=0)[0]

x = X[:, 0]
y = X[:, 1]

plt.figure(figsize=(10, 7))
plt.scatter(x, y)
plt.suptitle("blob")
plt.show

print("\nDBSCAN")
dbscan = cluster.DBSCAN(eps=0.2, min_samples=10, metric="euclidean")
labels = dbscan.fit_predict(X)
df_dbscan = pd.DataFrame(X)
df_dbscan["cluster"] = labels
df_dbscan.columns = ["axis_0", "axis_1", "cluster"]
display(df_dbscan["cluster"].value_counts().sort_index())

print("\nHDBSCAN")
hdbscan_ = hdbscan.HDBSCAN()
hdbscan_.fit(X)
df_hdbscan = pd.DataFrame(X)
df_hdbscan["cluster"] = hdbscan_.labels_
df_hdbscan.columns = ["axis_0", "axis_1", "cluster"]
display(df_hdbscan["cluster"].value_counts().sort_index())

plt.figure(figsize=(10, 3))
plt.suptitle("dbscan")
sns.scatterplot(x="axis_0", y="axis_1", hue="cluster", data=df_dbscan)

plt.figure(figsize=(10, 3))
plt.suptitle("hdbscan")
sns.scatterplot(x="axis_0", y="axis_1", hue="cluster", data=df_hdbscan)

# %%
