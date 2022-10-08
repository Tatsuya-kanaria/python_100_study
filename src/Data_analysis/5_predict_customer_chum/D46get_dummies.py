# %%
import D43continue_customer as D43
import D44predict_add_enrolled
import D45dropna

import pandas as pd


target_col = ["campaign_name", "class_name", "gender",
              "count_1", "routine_flg", "period", "is_deleted"]

predict_data = D43.predict_data[target_col]

# ダミー変数化
predict_data = pd.get_dummies(predict_data)

del predict_data["campaign_name_通常"]
del predict_data["class_name_ナイト"]
del predict_data["gender_M"]

predict_data.head()

# %%
