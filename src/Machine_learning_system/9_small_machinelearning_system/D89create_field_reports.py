# %%
import datetime
from dateutil.relativedelta import relativedelta
import os
import pandas as pd

import D86building_and_evaluating_models
from D81folder_creation_and_initial_variables import tg_ym, output_report_dir
from D82store_data_from_update_data import store_data
from D88predict_new_data import pred

target_cols = [
    'store_name',
    'order',
    'order_fin',
    'order_cancel',
    'order_delivery',
    'order_takeout',
    'order_weekday',
    'order_weekend',
    'delta_avg',
]

store_data = store_data[target_cols]
actual_cols = ['store_name']
rename_cols = [
    x + f'_{tg_ym}' for x in store_data.columns if x != 'store_name']
actual_cols.extend(rename_cols)
store_data.columns = actual_cols
store_data.head(3)

pred.loc[pred['score_weekday'] >= 0.75, 'オーダー予測 平日'] = '増加大'
pred.loc[(pred['score_weekday'] < 0.75) & (
    pred['score_weekday'] >= 0.5), 'オーダー予測 平日'] = '増加'
pred.loc[(pred['score_weekday'] < 0.5) & (
    pred['score_weekday'] >= 0.25), 'オーダー予測 平日'] = '減少'
pred.loc[(pred['score_weekday'] < 0.25), 'オーダー予測 平日'] = '減少大'

pred.loc[pred['score_weekend'] >= 0.75, 'オーダー予測 休日'] = '増加大'
pred.loc[(pred['score_weekend'] < 0.75) & (
    pred['score_weekend'] >= 0.5), 'オーダー予測 休日'] = '増加'
pred.loc[(pred['score_weekend'] < 0.5) & (
    pred['score_weekend'] >= 0.25), 'オーダー予測 休日'] = '減少'
pred.loc[(pred['score_weekend'] < 0.25), 'オーダー予測 休日'] = '減少大'

report = pred[[
    'store_name',
    'オーダー予測 平日',
    'オーダー予測 休日',
    'score_weekday',
    'score_weekend'
]]
report = pd.merge(report, store_data, on='store_name', how='left')

pred_ym = datetime.datetime.strptime(tg_ym, '%Y%m')
pred_ym = pred_ym + relativedelta(months=1)
pred_ym = datetime.datetime.strftime(pred_ym, '%Y%m')

report_name = f'report_pred_{pred_ym}.xlsx'
report.to_excel(os.path.join(output_report_dir, report_name), index=False)

# %%
