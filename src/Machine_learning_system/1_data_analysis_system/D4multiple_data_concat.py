# %%
import pandas as pd

import D3list_of_file_names as D3


order_all = pd.DataFrame()
for file in D3.tbl_order_files:
    order_data = pd.read_csv(file)
    if __name__ == '__main__':
        print(f'{file}:{len(order_data)}')

    order_all = pd.concat([order_all, order_data], ignore_index=True)

order_all

# %%
