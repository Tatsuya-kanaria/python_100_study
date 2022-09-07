# %%
import pandas as pd

import D11read_csv as D11


# 揺れを補正する
if __name__ == '__main__':
    # 補正前は99になる
    print(len(pd.unique(D11.uriage_data.item_name)))

D11.uriage_data["item_name"] = D11.uriage_data["item_name"].str.upper()
D11.uriage_data["item_name"] = D11.uriage_data["item_name"].str.replace(
    "　", "")
D11.uriage_data["item_name"] = D11.uriage_data["item_name"].str.replace(
    " ", "")
D11.uriage_data.sort_values(by=["item_name"], ascending=True)

if __name__ == '__main__':
    print(pd.unique(D11.uriage_data["item_name"]))
    print(len(pd.unique(D11.uriage_data["item_name"])))

# %%
