# %%
import pandas as pd

from D72data_read import tg_ym
from D74supports_categorical_variables import store_data
from D75format import X
from D76loading_the_model import models


model_weekday, model_weekend = models

pred_weekday = model_weekday.predict(X)
pred_weekend = model_weekend.predict(X)

pred_proba_weekday = model_weekday.predict_proba(X)
pred_proba_weekend = model_weekend.predict_proba(X)

pred_proba_weekday = pred_proba_weekday[:, 1]
pred_proba_weekend = pred_proba_weekend[:, 1]

pred = pd.DataFrame({
    'pred_weekday': pred_weekday,
    'pred_weekend': pred_weekend,
    'score_weekday': pred_proba_weekday,
    'score_weekend': pred_proba_weekend,
})

pred['store_name'] = store_data['store_name']
pred['year_month'] = tg_ym
pred.head(3)

# %%
