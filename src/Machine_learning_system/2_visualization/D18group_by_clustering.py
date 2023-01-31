# %%
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import D17data_processing_for_clustering as D17

sc = StandardScaler()
store_clustering_sc = sc.fit_transform(D17.store_clustering)

kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(store_clustering_sc)
D17.store_clustering['cluster'] = clusters.labels_
if __name__ == '__main__':
    print(D17.store_clustering['cluster'].unique())
D17.store_clustering.head()

# %%
