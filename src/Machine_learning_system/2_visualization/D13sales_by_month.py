# %%
import D11read_csv as D11
import D12get_the_big_picture

import pandas as pd


analyze_data = D11.analyze_data
read_columns = ['order_accept_date', 'delivered_date']

for old_column in read_columns:
    analyze_data[old_column] = pd.to_datetime(analyze_data[old_column])

    new_column = old_column.replace('date', 'month')

    analyze_data[new_column] = analyze_data[old_column].dt.strftime(
        '%Y%m')


analyze_data[['order_accept_date',
              'order_accept_month', 'delivered_month']].head()

analyze_data.dtypes
month_data = analyze_data.groupby('order_accept_month')
month_data.describe()

month_data.sum()

# %%
