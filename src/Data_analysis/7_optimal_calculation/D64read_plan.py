# %%
import pandas as pd


df_material = pd.read_csv('./data/product_plan_material.csv', index_col="製品")

df_profit = pd.read_csv('./data/product_plan_profit.csv', index_col="製品")

df_stock = pd.read_csv('./data/product_plan_stock.csv', index_col="項目")

df_plan = pd.read_csv('./data/product_plan.csv', index_col="製品")

if __name__ == '__main__':

    print(df_material)
    print(df_profit)
    print(df_stock)
    print(df_plan)

# %%
