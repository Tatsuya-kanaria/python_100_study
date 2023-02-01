# %%
import D17data_processing_for_clustering as D17
import D18group_by_clustering as D18


D17.store_clustering.columns = ['月内件数', '月内平均値',
                                '月内中央値', '月内最大値', '月内最小値', 'cluster']
D17.store_clustering.groupby('cluster').count()
D17.store_clustering.groupby('cluster').mean()

# %%
