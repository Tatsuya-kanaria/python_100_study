# %%
import pandas as pd


# データ読み込み
df_tr = pd.read_csv('./data/trans_route.csv', index_col="工場")
df_demand = pd.read_csv('./data/demand.csv')
df_supply = pd.read_csv('./data/supply.csv')

# 需要側の制約条件
for i in range(len(df_demand.columns)):
    temp_sum = sum(df_tr[df_demand.columns[i]])
    print(str(df_demand.columns[i])+"への輸送量:" +
          str(temp_sum)+"(需要量:"+str(df_demand.iloc[0][i])+")")

    if temp_sum >= df_demand.iloc[0][i]:
        print("需要量を満たしています。")
    else:
        print("需要量を満たしていません。輸送ルートを再計算して下さい。")

# 供給側の制約条件
for i in range(len(df_supply.columns)):
    temp_sum = sum(df_tr.loc[df_supply.columns[i]])
    print(str(df_supply.columns[i])+"からの輸送量:" +
          str(temp_sum)+"（供給限界:"+str(df_supply.iloc[0][i])+"）")
    if temp_sum <= df_supply.iloc[0][i]:
        print("供給限界の範囲内です。")
    else:
        print("供給限界を超過しています。輸送ルートを再計算してください。")

# %%
