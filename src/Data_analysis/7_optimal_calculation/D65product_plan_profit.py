# %%
import D64read_plan as D64


def product_plan(df_profit, df_plan):
    profit = 0
    for i in range(len(df_profit.index)):
        for j in range(len(df_plan.columns)):
            profit += df_profit.iloc[i][j] * df_plan.iloc[i][j]
    return profit


if __name__ == '__main__':
    print("総利益: " + str(product_plan(D64.df_profit, D64.df_plan)))

# %%
