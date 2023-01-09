# %%
import pandas as pd


# データ読み込み
df_tr = pd.read_csv('./data/trans_route.csv', index_col="工場")
df_tc = pd.read_csv('./data/trans_cost.csv', index_col="工場")

# 輸送コスト関数


def trans_cost(df_tr, df_tc):
    cost = 0
    for i in range(len(df_tc.index)):
        for j in range(len(df_tr.columns)):
            cost += df_tr.iloc[i][j]*df_tc.iloc[i][j]
    return cost


print("総輸送コスト:"+str(trans_cost(df_tr, df_tc)))

# %%