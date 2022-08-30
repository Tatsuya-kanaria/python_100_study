# %%
import pandas as pd
import D2concat as D2


join_data = pd.merge(D2.transaction_detail, D2.transaction[[
                     "transaction_id", "payment_date", "customer_id"]], on="transaction_id", how="left")

join_data.head()

if __name__ == "__main__":
    print(len(D2.transaction_detail))
    print(len(D2.transaction))
    print(len(join_data))

# %%
