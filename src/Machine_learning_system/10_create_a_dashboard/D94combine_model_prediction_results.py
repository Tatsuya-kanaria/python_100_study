# %%
import os
import pandas as pd

from D91single_data_load import output_report_dir


report_files = os.listdir(output_report_dir)
report_all = []
for report_file in report_files:
    report_file_path = os.path.join(output_report_dir, report_file)
    report_monthly = pd.read_excel(report_file_path)
    report_monthly = report_monthly[[
        'store_name',
        'score_weekday',
        'score_weekend'
    ]].copy()
    report_monthly['files'] = report_file
    report_all.append(report_monthly)
report_all = pd.concat(report_all, ignore_index=True)

report_all['pred_year_month'] = report_all['files'].str.split('.', expand=True)[
    0]
report_all['pred_year_month'] = report_all['pred_year_month'].str[-6:]

report_all.head()

# %%
