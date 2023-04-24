# %%
import pandas as pd

from D81folder_creation_and_initial_variables import tg_ym
from D82store_data_from_update_data import store_data
from D87preparing_for_prediction import X, model_weekday, model_weekend


pred_weekday = model_weekday.predict(X)
pred_weekend = model_weekend.predict(X)

pred_proba_weekday = model_weekday.predict_proba(X)[:, 1]
pred_proba_weekend = model_weekend.predict_proba(X)[:, 1]

pred = pd.DataFrame(
    {'pred_weekday': pred_weekday,
     'pred_weekend': pred_weekend,
     'score_weekday': pred_proba_weekday,
     'score_weekend': pred_proba_weekend}
)
pred['store_name'] = store_data['store_name']
pred['year_month'] = tg_ym
pred.head(3)

# %%
