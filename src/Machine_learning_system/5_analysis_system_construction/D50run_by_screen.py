# %%
from D41basic_folder_generation import input_dir
from D42check_mechanism import init_tran_df, m_store, m_area
from D46make_active_folder import make_active_folder
from D48dynamic_loading_previous import make_report_hq_r2, make_report_store_r2

from IPython.display import display, clear_output
from ipywidgets import DatePicker
import os
import datetime
import pandas as pd


def order_by_date(val):
    clear_output()
    display(date_picker)

    df_array = []

    print('データ確認、データ準備開始・・・')

    date_str = str(val['new'])
    date_dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    target_ym = date_dt.strftime('%Y%m')

    # フォルダの動的生成
    target_output_dir = make_active_folder(target_ym)

    # 選択された基準月のデータ確認
    target_file = "tbl_order_" + target_ym + ".csv"
    if os.path.exists(os.path.join(input_dir, target_file)) == False:
        print(f'{target_file}が存在しません')
        return
    else:
        # データの読み込み
        df = pd.read_csv(os.path.join(input_dir, target_file))
        df = init_tran_df(df)
        df_array.append(df)

    # 選択された基準付きの1月前があるか確認
    target_ym_old = str(int(target_ym) - 1)
    target_file = "tbl_order_" + target_ym_old + ".csv"
    if os.path.exists(os.path.join(input_dir, target_file)) == True:
        # データがある場合のみ
        df = pd.read_csv(os.path.join(input_dir, target_file))
        df = init_tran_df(df)
        df_array.append(df)

    print('データ準備完了、レポーティング出力開始・・・')
    # 本部向けレポートR2を呼ぶ
    make_report_hq_r2(df_array, target_output_dir)

    print('管理レポート出力完了、各店舗のレポーティング出力開始・・・')

    # # 各店舗向けレポート（全店舗実施）
    for store_id in m_store.loc[m_store['store_id'] != 999]['store_id']:
        # narrow_areaのフォルダを作成
        area_cd = m_store.loc[m_store['store_id'] == store_id]['area_cd']
        area_name = m_area.loc[m_area['area_cd'] ==
                               area_cd.values[0]]['narrow_area'].values[0]
        target_store_output_dir = os.path.join(target_output_dir, area_name)
        os.makedirs(target_store_output_dir, exist_ok=True)
        make_report_store_r2(df_array, store_id, target_store_output_dir)

    print('処理完了しました。')


date_picker = DatePicker(value=datetime.datetime(2020, 4, 1))
date_picker.observe(order_by_date, names='value')
print('データを0_inputフォルダにコピーした後、基準月を選択して下さい。')
display(date_picker)

# %%
