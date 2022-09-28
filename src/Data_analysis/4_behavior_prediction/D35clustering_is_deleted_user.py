# %%
import D31read_data as D31
import D32clustering_customer as D32
import D33clustering_analysis

import pandas as pd


customer_clustering = pd.concat(
    [D32.customer_clustering, D31.customer], axis=1)
customer_clustering.groupby(["cluster", "is_deleted"], as_index=False).count()[
    ["cluster", "is_deleted", "customer_id"]]

customer_clustering.groupby(["cluster", "routine_flg"], as_index=False).count()[
    ["cluster", "routine_flg", "customer_id"]]

# %%
