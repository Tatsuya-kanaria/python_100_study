# %%
import pandas as pd

import D11read_csv as D11
import D13shaking_tally
import D14shake_correction
import D15missing_imputation
import D16kokyaku_shake
import D17date_shake


# 結合
join_data = pd.merge(D11.uriage_data, D11.kokyaku_data,
                     left_on="customer_name", right_on="顧客名", how="left")
join_data = join_data.drop("customer_name", axis=1)
join_data

# %%
