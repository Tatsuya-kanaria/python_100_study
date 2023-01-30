# %%
import japanize_matplotlib
import D13sales_by_month as D13

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

pre_data = pd.pivot_table(D13.analyze_data, index='order_accept_month',
                          columns='narrow_area', values='total_amount', aggfunc='mean')

pre_data

narrow_area = set(D13.analyze_data['narrow_area'])

if __name__ == '__main__':
    print(narrow_area)

for area in narrow_area:
    plt.plot(list(pre_data.index), pre_data[area], label=area)

plt.legend()

# %%
