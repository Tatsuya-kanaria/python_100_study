# %%
from D41basic_folder_generation import input_dir
from D42check_mechanism import target_data, m_store, m_area, tg_ym, init_tran_df

from D46make_active_folder import target_output_dir
from D48dynamic_loading_previous import make_report_hq_r2, make_report_store_r2

import pandas as pd
import os


tg_ym_old = str(int(tg_ym) - 1)
target_file = "tbl_order_" + tg_ym_old + ".csv"
target_data_old = pd.read_csv(os.path.join(input_dir, target_file))

# 過去分を初期化
target_data_old = init_tran_df(target_data_old)

df_array = [target_data, target_data_old]

# フォルダの動的生成
# target_output_dir = make_active_folder(tg_ym)

# 本部向けレポートを呼ぶ
make_report_hq_r2(df_array, target_output_dir)

# 各店舗向けレポート（全店舗実施）
for store_id in m_store.loc[m_store['store_id'] != 999]['store_id']:
    # narrow_areaのフォルダを作成
    area_cd = m_store.loc[m_store['store_id'] == store_id]['area_cd']
    area_name = m_area.loc[
        m_area['area_cd'] == area_cd.values[0]
    ]['narrow_area'].values[0]
    target_store_output_dir = os.path.join(target_output_dir, area_name)
    os.makedirs(target_store_output_dir, exist_ok=True)
    make_report_store_r2(df_array, store_id, target_store_output_dir)

# %%
