# %%
import D43continue_customer as D43

import pandas as pd
from dateutil.relativedelta import relativedelta


D43.predict_data["period"] = 0
D43.predict_data["now_date"] = pd.to_datetime(
    D43.predict_data["年月"], format="%Y%m")

D43.predict_data["start_date"] = pd.to_datetime(D43.predict_data["start_date"])

for i in range(len(D43.predict_data)):
    delta = relativedelta(
        D43.predict_data["now_date"][i], D43.predict_data["start_date"][i])
    D43.predict_data["period"][i] = int(delta.years*12 + delta.months)

D43.predict_data.head()

# %%
