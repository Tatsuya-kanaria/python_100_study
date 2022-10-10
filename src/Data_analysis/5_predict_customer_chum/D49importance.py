# %%
import D48model_tuning as D48
import D49_1_tree_graphviz as D49

import pandas as pd


# 重要変数
importance = pd.DataFrame(
    {"reature_names": D48.X.columns, "coefficient": D48.model.feature_importances_})

importance

# %%
