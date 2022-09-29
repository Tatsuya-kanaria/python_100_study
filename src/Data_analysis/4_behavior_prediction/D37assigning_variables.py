# %%
import D31read_data as D31
import D36forecast_preparation as D36

import pandas as pd
from dateutil.relativedelta import relativedelta


D36.predict_data = pd.merge(D36.predict_data, D31.customer[[
                            "customer_id", "start_date"]], on="customer_id", how="left")

D36.predict_data["now_date"] = pd.to_datetime(
    D36.predict_data["年月"], format="%Y%m")

D36.predict_data["start_date"] = pd.to_datetime(D36.predict_data["start_date"])

D36.predict_data["period"] = None
for i in range(len(D36.predict_data)):
    delta = relativedelta(
        D36.predict_data["now_date"][i], D36.predict_data["start_date"][i])

    D36.predict_data["period"][i] = delta.years*12 + delta.months

D36.predict_data.head()

# %%
