# %%
from sklearn.manifold import TSNE
import pandas as pd
import seaborn as sns

import D17data_processing_for_clustering as D17
import D18group_by_clustering as D18

tsne = TSNE(n_components=2, random_state=0)
x = tsne.fit_transform(D18.store_clustering_sc)
tsne_df = pd.DataFrame(x)
tsne_df['cluster'] = D17.store_clustering['cluster']
tsne_df.columns = ['axis_0', 'axis_1', 'cluster']
tsne_df.head()

tsne_graph = sns.scatterplot(
    x='axis_0', y='axis_1', hue='cluster', data=tsne_df)

# %%
