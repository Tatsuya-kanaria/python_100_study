# %%
import pandas as pd


customer = pd.read_csv('./data/customer_join.csv')
uselog_months = pd.read_csv('./data/use_log_months.csv')

# 年月リスト
year_months = list(uselog_months["年月"].unique())
uselog = pd.DataFrame()

for i in range(1, len(year_months)):
    tmp = uselog_months.loc[uselog_months["年月"] == year_months[i]]
    tmp.rename(columns={"count": "count_0"}, inplace=True)
    tmp_before = uselog_months.loc[uselog_months["年月"] == year_months[i-1]]
    del tmp_before["年月"]
    tmp_before.rename(columns={"count": "count_1"}, inplace=True)
    tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")
    uselog = pd.concat([uselog, tmp], ignore_index=True)

uselog.head()

# %%
