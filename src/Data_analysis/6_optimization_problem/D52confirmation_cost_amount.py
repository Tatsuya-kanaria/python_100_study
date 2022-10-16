# %%
import D51read_csv as D51

import pandas as pd


kanto_tmp = (D51.kanto["Cost"].sum() / D51.kanto["Quantity"].sum()) *10000
tohoku_tmp = (D51.tohoku["Cost"].sum() / D51.tohoku["Quantity"].sum()) *10000

cost_chk = pd.merge(D51.cost, D51.factories, on="FCID", how="left")



if __name__ == '__main__':
    print("関東支社の総コスト：" + str(D51.kanto["Cost"].sum()) + "万円")
    print("東北支社の総コスト：" + str(D51.tohoku["Cost"].sum()) + "万円")

    print("関東支社の総部品輸送個数：" + str(D51.kanto["Quantity"].sum()) + "個")
    print("東北支社の総部品輸送個数：" + str(D51.tohoku["Quantity"].sum()) + "個")


    print("関東支社の部品1つ当たりの輸送コスト:" + str(int(kanto_tmp)) + "円")
    print("東北支社の部品1つ当たりの輸送コスト:" + str(int(tohoku_tmp)) + "円")

    print("関東支社の平均輸送コスト" + str(cost_chk["Cost"].loc[cost_chk["FCRegion"]=="関東"].mean()) + "万円")
    print("東北支社の平均輸送コスト" + str(cost_chk["Cost"].loc[cost_chk["FCRegion"]=="東北"].mean()) + "万円")


# %%
