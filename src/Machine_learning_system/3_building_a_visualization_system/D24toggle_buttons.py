# %%
from ipywidgets import ToggleButtons
from IPython.display import display, clear_output
import pandas as pd

from D21filter_and_visualize import order_data, m_area


area_list = m_area['wide_area'].unique()


def order_by_area(val):
    clear_output()
    display(toggle)
    pick_data = order_data.loc[(order_data['wide_area'] == val['new']) & (
        order_data['status'].isin([1, 2]))]

    display(pick_data.head())


toggle = ToggleButtons(options=area_list)
print(toggle)
toggle.observe(order_by_area, names='value')
display(toggle)


def graph_by_area(val):
    clear_output()
    display(toggle2)
    pick_data = order_data.loc[(order_data['wide_area'] == val['new']) & (
        order_data['status'].isin([1, 2]))]
    temp = pick_data[['order_accept_date', 'total_amount']].copy()
    temp.loc[:, 'order_accept_date'] = pd.to_datetime(
        temp['order_accept_date'])
    temp.set_index('order_accept_date', inplace=True)
    temp.resample('D').sum().plot()


toggle2 = ToggleButtons(options=area_list)
toggle2.observe(graph_by_area, names='value')
display(toggle2)

# %%
