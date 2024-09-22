# %%

import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
from pandas import plotting
import pandas as pd
import matplotlib.pyplot as plt

df_wine = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df_wine.columns = ["class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids",
                   "Nonflavanoid phenols", "Pronathocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
display(df_wine.shape)
display(df_wine.head())


# plotting.scatter_matrix(df_wine.iloc[:, 1:], figsize=(
#     8, 8), c=list(df_wine.iloc[:, 0]), alpha=0.5)
# plt.show


sc = preprocessing.StandardScaler()
X = df_wine.iloc[:, 1:]
X_norn = sc.fit_transform(X)

pca = PCA(random_state=0)
X_pc = pca.fit_transform(X_norn)
df_pca = pd.DataFrame(
    X_pc, columns=["PC{}".format(i + 1) for i in range(len(X_pc[0]))])
print("主成分の数", pca.n_components_)
print("保たれている情報", round(np.sum(pca.explained_variance_ratio_), 2))
display(df_pca.head())

pd.DataFrame(np.round(pca.explained_variance_, 2),
             index=["PC{}".format(x + 1) for x in range(len(df_pca.columns))], columns=["固有値"])

line = np.ones(14)
plt.plot(np.append(np.nan, pca.explained_variance_), "s-")
plt.plot(line, "s-")
plt.xlabel("PC")
plt.ylabel("explained_variance")
plt.xticks(np.arange(1, 14, 1))
plt.grid()
plt.show()

# %%
