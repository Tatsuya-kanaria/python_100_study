# %%
import D31read_data as D31

import pandas as pd


D31.uselog["usedate"] = pd.to_datetime(D31.uselog["usedate"])
D31.uselog["年月"] = D31.uselog["usedate"].dt.strftime("%Y%m")
uselog_months = D31.uselog.groupby(
    ["年月", "customer_id"], as_index=False).count()
uselog_months.rename(columns={"log_id": "count"}, inplace=True)
del uselog_months["usedate"]
uselog_months.head()

year_months = list(uselog_months["年月"].unique())
predict_data = pd.DataFrame()

for i in range(6, len(year_months)):
    tmp = uselog_months.loc[uselog_months["年月"] == year_months[i]]
    tmp.rename(columns={"count": "count_pred"}, inplace=True)
    for j in range(1, 7):
        tmp_before = uselog_months.loc[uselog_months["年月"] == year_months[i-j]]
        del tmp_before["年月"]
        tmp_before.rename(
            columns={"count": "count_{}".format(j-1)}, inplace=True)
        tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")

    predict_data = pd.concat([predict_data, tmp], ignore_index=True)

predict_data = predict_data.dropna()
predict_data = predict_data.reset_index(drop=True)
predict_data.head()

# %%
