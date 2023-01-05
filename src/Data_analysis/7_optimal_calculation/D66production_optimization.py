# %%
import pandas as pd
from pulp import LpVariable, lpSum, value
from ortoolpy import model_max, addvars, addvals

import D64read_plan as D64


df = D64.df_material.copy()
inv = D64.df_stock

m = model_max()
v1 = {(i): LpVariable('v%d' % (i), lowBound=0)
      for i in range(len(D64.df_profit))}
m += lpSum(D64.df_profit.iloc[i] * v1[i] for i in range(len(D64.df_profit)))
for i in range(len(D64.df_material.columns)):
    m += lpSum(D64.df_material.iloc[j, i] * v1[j]
               for j in range(len(D64.df_profit))) <= D64.df_stock.iloc[:, i]
m.solve()

df_plan_sol = D64.df_plan.copy()
for k, x in v1.items():
    df_plan_sol.iloc[k] = value(x)
print(df_plan_sol)
print("総利益: " + str(value(m.objective)))

# %%
