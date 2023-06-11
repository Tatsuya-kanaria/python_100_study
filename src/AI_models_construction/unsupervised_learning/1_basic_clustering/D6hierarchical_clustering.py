
# %%
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import linkage


X = load_iris().data[::10, 2:4]
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1, title="iris")


plt.scatter(X[:, 0], X[:, 1])
for i, element in enumerate(X):
    plt.text(element[0]+0.02, element[1]+0.02, i)
plt.show()

Z = linkage(X, method="ward", metric="euclidean")
pd.DataFrame(Z)

# %%
