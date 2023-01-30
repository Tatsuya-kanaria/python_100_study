# %%
import seaborn as sns

import D13sales_by_month as D13


store_clustering = D13.analyze_data.groupby('store_id').agg(
    ['size', 'mean', 'median', 'max', 'min'])['total_amount']

store_clustering.reset_index(inplace=True, drop=True)
print(len(store_clustering))

store_clustering.head()

# kind : グラフの種類 kde:密度
hexbin = sns.jointplot(x='mean', y='size', data=store_clustering, kind='hex')

# %%
