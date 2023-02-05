# %%
from ipywidgets import SelectMultiple
from IPython.display import display, clear_output
import japanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

import D21filter_and_visualize as D21


order_data = D21.order_data
store_list = D21.store_list


def order_by_multi(val):
    clear_output()
    display(select)
    pick_data = order_data.loc[(order_data['store_name'].isin(
        val['new'])) & (order_data['status'].isin([1, 2]))]
    display(pick_data.head())


select = SelectMultiple(options=store_list)
select.observe(order_by_multi, names='value')
display(select)


def graph_by_multi(val):
    clear_output()
    display(select2)

    fig = plt.figure(figsize=(17, 4))
    plt.subplots_adjust(wspace=0.25, hspace=0.6)

    i = 0

    for trg in val['new']:
        pick_data = order_data[(order_data['store_name'] == trg) & (
            order_data['status'].isin([1, 2]))]
        temp = pick_data[['order_accept_date',
                          'total_amount', 'store_name']].copy()
        temp.loc[:, 'order_accept_date'] = pd.to_datetime(
            temp['order_accept_date'])
        temp.set_index('order_accept_date', inplace=True)
        i += 1
        ax = fig.add_subplot(1, len(val['new']), i)
        ax.plot(temp.resample('D').sum())
        ax.set_title(trg)


select2 = SelectMultiple(options=store_list)
select2.observe(graph_by_multi, names='value')
display(select2)

# %%
