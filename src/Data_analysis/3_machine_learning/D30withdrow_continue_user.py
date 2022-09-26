# %%
import D28membership_period
import D27log_customer_merge as D27


customer_end = D27.customer_join.loc[D27.customer_join["is_deleted"] == 1]

customer_end.describe()

customer_stay = D27.customer_join.loc[D27.customer_join["is_deleted"] == 0]

customer_stay.describe()

# 出力

D27.customer_join.to_csv("./data/customer_join.csv", index=False)

# %%
