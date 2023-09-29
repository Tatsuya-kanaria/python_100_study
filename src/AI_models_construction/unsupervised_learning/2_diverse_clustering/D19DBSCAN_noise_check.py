# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from D18DBSCAN_clustering import labels, X


pd.DataFrame(labels)[0].value_counts().sort_index()

df_dbscan = pd.DataFrame(X)
df_dbscan["cluster"] = labels
df_dbscan.columns = ["axis_0", "axis_1", "cluster"]
df_dbscan.head()
plt.figure(figsize=(10, 3))
sns.scatterplot(x="axis_0", y="axis_1", hue="cluster", data=df_dbscan)


# %%
