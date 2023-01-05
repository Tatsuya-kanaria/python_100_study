# %%
import numpy as np

import D64read_plan as D64
import D66production_optimization as D66


def condition_stock(df_plan, df_material, df_stock):
    flag = np.zeros(len(df_material.columns))
    for i in range(len(df_material.columns)):
        temp_sum = 0
        for j in range(len(df_material.index)):

            temp_sum = temp_sum + \
                df_material.iloc[j][i] * float(df_plan.iloc[j])
        if (temp_sum <= float(df_stock.iloc[0][i])):
            flag[i] = 1
        print(df_material.columns[i] + " 使用量:" + str(temp_sum) +
              ", 在庫:" + str(float(df_stock.iloc[0][i])))
    return flag


if __name__ == "__main__":
    print("制約条件計算結果:" +
          str(condition_stock(D66.df_plan_sol, D64.df_material, D64.df_stock)))

# %%
