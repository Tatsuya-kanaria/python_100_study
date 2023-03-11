# %%
from D42check_mechanism import target_data, m_store, m_area
from D43headquarters_reportiong_function import make_report_hq
from D44stores_reporting_function import make_report_store
from D46make_active_folder import target_output_dir

import os


# 本部向けレポート（出力先変更）
make_report_hq(target_data, target_output_dir)

# 各店舗向けれレポート（全店舗実施）
for store_id in m_store.loc[m_store['store_id'] != 999]['store_id']:
    # narrow_areaのフォルダを作成
    area_cd = m_store.loc[
        m_store['store_id'] == store_id]['area_cd']
    area_name = m_area.loc[
        m_area['area_cd'] == area_cd.values[0]]['narrow_area'].values[0]
    target_store_output_dir = os.path.join(target_output_dir, area_name)
    os.makedirs(target_store_output_dir, exist_ok=True)
    make_report_store(target_data, store_id, target_store_output_dir)

# %%
