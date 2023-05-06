# %%
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
# %matplotlib inline

import seaborn as sns

from sklearn.cluster import KMeans

from IPython.display import display

iris = load_iris()
iris.data.shape
print(iris.target_names)

df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris.describe()

df_temp = df_iris.copy()
sns.pairplot(df_temp)

model = KMeans(n_clusters=3, random_state=0, init="random", n_init=10)
cls_data = df_iris.copy()
model.fit(cls_data)

cluster = model.predict(cls_data)
if __name__ == '__main__':
    print(cluster)

cls_data["cluster"] = cluster
sns.pairplot(cls_data, hue="cluster")

cluster_center = pd.DataFrame(model.cluster_centers_)
cluster_center.columns = cls_data.columns[:4]

if __name__ == '__main__':
    display(cluster_center)

plt.scatter(cls_data["sepal length (cm)"],
            cls_data["sepal width (cm)"], c=cls_data["cluster"])
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.scatter(cluster_center["sepal length (cm)"],
            cluster_center["sepal width (cm)"], marker="*", color="red")

display(cls_data.groupby("cluster").mean().round(2))

cls_data["target"] = iris.target
cls_data.loc[cls_data["target"] == 0, "target"] = "setosa"
cls_data.loc[cls_data["target"] == 1, "target"] = ""
cls_data.loc[cls_data["target"] == 2, "target"] = "virginica"

display(cls_data.groupby("target").mean().round(2))

# %%
