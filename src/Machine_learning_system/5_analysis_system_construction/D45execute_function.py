# %%
from D41basic_folder_generation import output_dir
from D42check_mechanism import target_data, m_store
from D43headquarters_reportiong_function import make_report_hq
from D44stores_reporting_function import make_report_store

# 本部向けレポート
make_report_hq(target_data, output_dir)

# 各店舗向けレポート(全店舗実施)
for store_id in m_store.loc[m_store['store_id'] != 999]['store_id']:
    make_report_store(target_data, store_id, output_dir)

# %%
