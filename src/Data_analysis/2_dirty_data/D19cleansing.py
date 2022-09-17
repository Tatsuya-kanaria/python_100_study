# %%
import pandas as pd

import D18merge as D18

# 整列
dump_data = D18.join_data[["purchase_date", "purchase_month",
                           "item_name", "item_price", "顧客名", "かな", "地域", "メールアドレス", "登録日"]]
dump_data

if __name__ == '__main__':
    # データ出力
    dump_data.to_csv("./data/dump_data.csv", index=False)

# %%
