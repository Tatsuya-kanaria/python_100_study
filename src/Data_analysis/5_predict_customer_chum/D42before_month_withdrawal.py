# %%
import D41read_formatting as D41

from dateutil.relativedelta import relativedelta
import pandas as pd


exit_customer = D41.customer.loc[D41.customer["is_deleted"] == 1]
exit_customer["exit_date"] = None
exit_customer["end_date"] = pd.to_datetime(exit_customer["end_date"])
exit_customer["exit_date"] = pd.to_datetime(exit_customer["exit_date"])

for i in range(len(exit_customer)):
    exit_customer["exit_date"].iloc[i] = exit_customer["end_date"].iloc[i] - \
        relativedelta(months=1)

exit_customer["年月"] = exit_customer["exit_date"].dt.strftime("%Y%m")
D41.uselog["年月"] = D41.uselog["年月"].astype(str)
exit_uselog = pd.merge(D41.uselog, exit_customer, on=[
                       "customer_id", "年月"], how="left")

exit_uselog = exit_uselog.dropna(subset=["name"])

if __name__ == '__main__':
    print(len(D41.uselog))
    print(len(exit_uselog))
    print(exit_uselog["customer_id"].unique())

exit_uselog.head()


# %%
