# %%
import D32clustering_customer as D32
import D33clustering_analysis

from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


X = D32.customer_clustering_sc
# モデルの定義
pca = PCA(n_components=2)
# 主成分分析
pca.fit(X)
x_pca = pca.transform(X)
# df内の0と1の意味
pca_df = pd.DataFrame(x_pca)
pca_df["cluster"] = D32.customer_clustering["cluster"]

for i in D32.customer_clustering["cluster"].unique():
    tmp = pca_df.loc[pca_df["cluster"] == i]
    plt.scatter(tmp[0], tmp[1])

# %%
