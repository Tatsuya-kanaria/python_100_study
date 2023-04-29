# %%
from dateutil.relativedelta import relativedelta
import pandas as pd

from D91single_data_load import ml_base_data
from D94combine_model_prediction_results import report_all


ml_data = ml_base_data[[
    'store_name',
    'y_weekday',
    'y_weekend',
    'year_month'
]].copy()
ml_data['pred_year_month'] = pd.to_datetime(
    ml_data['year_month'], format='%Y%m')
ml_data['pred_year_month'] = ml_data['pred_year_month'].map(
    lambda x: x + relativedelta(months=1))
ml_data['pred_year_month'] = ml_data['pred_year_month'].dt.strftime('%Y%m')
del ml_data['year_month']
ml_data.head(3)

report_valid = pd.merge(
    report_all, ml_data, on=[
        'store_name',
        'pred_year_month'
    ], how='left'
)

report_valid.dropna(inplace=True)
report_valid.isna().all()

# %%
