# %%
import D32clustering_customer as D32


D32.customer_clustering.columns = [
    "月内平均値", "月内中央値", "月内最大値", "月内最小値", "会員期間", "cluster"]

D32.customer_clustering.groupby("cluster").count()

D32.customer_clustering.groupby("cluster").mean()

# %%
