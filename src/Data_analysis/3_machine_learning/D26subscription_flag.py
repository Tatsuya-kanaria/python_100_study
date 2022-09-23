# %%
import D21read as D21
import D25uselog_aggregation as D25


# 曜日別
D21.uselog["weekday"] = D21.uselog["usedate"].dt.weekday
uselog_weekday = D21.uselog.groupby(["customer_id", "年月", "weekday"], as_index=False).count()[
    ["customer_id", "年月", "weekday", "log_id"]]
uselog_weekday.rename(columns={"log_id": "count"}, inplace=True)
uselog_weekday.head()

#
uselog_weekday = uselog_weekday.groupby("customer_id", as_index=False).max()[
    ["customer_id", "count"]]
uselog_weekday["routine_flg"] = 0
uselog_weekday["routine_flg"] = uselog_weekday["routine_flg"].where(
    uselog_weekday["count"] < 4, 1)
uselog_weekday.head()

# %%
