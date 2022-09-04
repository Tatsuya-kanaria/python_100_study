# %%
import pandas as pd

import D5create_column as D5
from D4merge2 import join_data

join_data.dtypes

# 年月列の作成
join_data['payment_date'] = pd.to_datetime(join_data['payment_date'])
join_data['payment_month'] = join_data['payment_date'].dt.strftime('%Y%m')
join_data[['payment_date', 'payment_month']].head()

join_data.groupby('payment_month').sum()['price']

# %%
