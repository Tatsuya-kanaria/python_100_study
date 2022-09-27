# %%
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import D31read_data as D31


customer_clustering = D31.customer[[
    "mean", "median", "max", "min", "membership_period"]]
customer_clustering.head()

sc = StandardScaler()
customer_clustering_sc = sc.fit_transform(customer_clustering)

kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(customer_clustering_sc)
customer_clustering["cluster"] = clusters.labels_

if __name__ == '__main__':
    # labelの種類確認
    print(customer_clustering["cluster"].unique())

customer_clustering.head()

# %%
