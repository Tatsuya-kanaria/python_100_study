# %%
import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sns
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import numpy as np
from IPython.display import display


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
df.loc[df["target"] == 0, "target_name"] = "setosa"
df.loc[df["target"] == 1, "target_name"] = "versicolor"
df.loc[df["target"] == 2, "target_name"] = "virginica"
df.head()

sns.pairplot(df, vars=df.columns[:4], hue="target_name")

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1, projection="3d")
for c in df["target_name"].unique():
    ax.scatter(
        df.iloc[:, 0][df["target_name"] == c],
        df.iloc[:, 1][df["target_name"] == c],
        df.iloc[:, 2][df["target_name"] == c],
        label=c
    )

ax.set_title("iris 3D")
ax.set_xlabel("sepal_length")
ax.set_ylabel("sepal_width")
ax.set_zlabel("petal_length")
ax.legend(loc=2, title="legend", shadow=True)
plt.show()

pca = PCA(random_state=0)
X_pc = pca.fit_transform(df.iloc[:, 0:4])
df_pca = pd.DataFrame(
    X_pc, columns=["PC{}".format(i + 1) for i in range(len(X_pc[0]))])

print("主成分の数: ", pca.n_components_)
print("保たれている情報: ", np.sum(pca.explained_variance_ratio_))
display(df_pca.head())

sns.scatterplot(x="PC1", y="PC2", data=df_pca, hue=df["target_name"])

# %%
