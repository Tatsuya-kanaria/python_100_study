# %%
from D31output_in_excel import m_store, order_all
from D38output_required_data import make_data_sheet
from D39summary_sheet_creation import make_summary_sheet

import os


os.makedirs('output', exist_ok=True)

for store in m_store['store_id'].tolist():
    if store != 999:
        store_df = order_all.loc[order_all['store_id'] == store]
        store_name = m_store.loc[m_store['store_id'] == store]['store_name']
        print(store_name)

        tmp_file_name = make_data_sheet(store, store_df, 'output')
        make_summary_sheet(store, store_name.values[0], tmp_file_name)

print('出力完了しました。')

# %%
