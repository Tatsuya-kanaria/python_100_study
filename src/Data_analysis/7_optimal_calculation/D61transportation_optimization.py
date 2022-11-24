# %%
import numpy as np
import pandas as pd
from itertools import product
from pulp import LpVariable, lpSum, value
from ortoolpy import model_min, addvars, addvals


# データ読み込み
df_tc = pd.read_csv('./data/trans_cost.csv', index_col="工場")
df_demand = pd.read_csv('./data/demand.csv')
df_supply = pd.read_csv('./data/supply.csv')

# 初期設定 #
'''pr
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
'''
np.random.seed(1)
nw = len(df_tc.index)
nf = len(df_tc.columns)
pr = list(product(range(nw), range(nf)))

# 数理モデル作成 #
ml = model_min()
'''vl
{(0, 0): v0_0, (0, 1): v0_1, (0, 2): v0_2, (0, 3): v0_3, (1, 0): v1_0, (1, 1): v1_1, (1, 2): v1_2, (1, 3): v1_3, (2, 0): v2_0, (2, 1): v2_1, (2, 2): v2_2, (2, 3): v2_3}
'''
vl = {(i, j): LpVariable('v%d_%d' % (i, j), lowBound=0) for i, j in pr}

'''ml
NoName:
MINIMIZE
447
VARIABLES
'''
ml += lpSum(df_tc.iloc[i][j]*vl[i, j] for i, j in pr)

for i in range(nw):
    ml += lpSum(vl[i, j] for j in range(nf)) <= df_supply.iloc[0][i]
for j in range(nf):
    ml += lpSum(vl[i, j] for i in range(nw)) >= df_demand.iloc[0][j]

ml.solve()

# 総輸送コスト計算 #
df_tr_sol = df_tc.copy()
total_cost = 0

for k, x in vl.items():
    i, j = k[0], k[1]
    df_tr_sol.iloc[i][j] = value(x)
    total_cost += df_tc.iloc[i][j] * value(x)
if __name__ == '__main__':
    print(df_tr_sol)
    print("総輸送コスト:"+str(total_cost))

# %%
