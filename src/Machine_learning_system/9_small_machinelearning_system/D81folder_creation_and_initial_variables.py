# %%
import os


data_dir = 'data'

input_dir = os.path.join(data_dir, '00_input')
score_monthly_dir = os.path.join(data_dir, '01_store_monthly')
ml_base_dir = os.path.join(data_dir, '02_ml_base')

output_ml_result_dir = os.path.join(data_dir, '10_output_ml_result')
output_report_dir = os.path.join(data_dir, '11_output_report')

master_dir = os.path.join(data_dir, '99_master')
model_dir = 'models'

os.makedirs(input_dir, exist_ok=True)
os.makedirs(score_monthly_dir, exist_ok=True)
os.makedirs(ml_base_dir, exist_ok=True)
os.makedirs(output_ml_result_dir, exist_ok=True)
os.makedirs(output_report_dir, exist_ok=True)
os.makedirs(master_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)

tg_ym = '202004'

target_file = "tbl_order_" + tg_ym + ".csv"
m_area_file = 'm_area.csv'
m_store_file = 'm_store.csv'
store_monthly_file = 'store_monthly_data.csv'
ml_base_file = 'ml_base_data.csv'


# %%
