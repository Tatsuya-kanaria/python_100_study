# %%
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram


X = load_iris().data[::10]

fig = plt.figure(figsize=(6, 3))
ax = fig.add_subplot(1, 1, 1, title="iris")
plt.scatter(X[:, 0], X[:, 1])
for i, element in enumerate(X):
    plt.text(element[0]+0.02, element[1]+0.02, i)
plt.show()

linkage_methods = ["complete", "ward"]

for method in linkage_methods:
    Z = linkage(X, method=method, metric="euclidean")
    fig, ax = plt.subplots(figsize=(6, 3))
    ax = dendrogram(Z)
    fig.suptitle(method)
    fig.show()

# %%
