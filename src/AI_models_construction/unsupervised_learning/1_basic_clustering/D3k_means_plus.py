# %%
import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.metrics import adjusted_rand_score


iris = load_iris()

df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)

cls_data = df_iris.copy()


def format_print(index, target, cls):
    format = "{}: {:.2f}".format(
        index,
        adjusted_rand_score(
            target, cls
        )
    )
    print(format)


# n_cluster 3
model = KMeans(
    n_clusters=3,
    random_state=0,
    init="k-means++",
    n_init=10
)
model.fit_predict(cls_data)

cluster = model.predict(cls_data)
cls_data["cluster"] = cluster

sns.pairplot(cls_data, hue="cluster")

format_print("ARI(n_cls 3)", iris.target, cls_data["cluster"])


# n_cluster 2
model = KMeans(
    n_clusters=2,
    random_state=0,
    init="k-means++",
    n_init=10
)
cls_data["cluster"] = model.fit_predict(cls_data)

sns.pairplot(cls_data, hue="cluster")

format_print("ARI(n_cls 2)", iris.target, cls_data["cluster"])

# %%
