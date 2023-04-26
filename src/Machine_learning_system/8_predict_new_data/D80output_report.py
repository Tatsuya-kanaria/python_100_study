# %%
import os
import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta

from D71folder_generation import output_dir
from D72data_read import tg_ym
from D77predict import pred
from D79create_of_performance_data import actual_data


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
report = pd.merge(report, actual_data, on='store_name', how='left')

report.head(3)

pred_ym = datetime.datetime.strptime(tg_ym, '%Y%m')
pred_ym = pred_ym + relativedelta(monts=1)
pred_ym = datetime.datetime.strftime(pred_ym, '%Y%m')

report_name = f'report_pred_{pred_ym}.xlsx'
report.to_excel(os.path.join(output_dir, report_name), index=False)

# %%
