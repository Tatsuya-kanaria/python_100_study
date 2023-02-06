# %%
from ipywidgets import IntSlider
from IPython.display import display, clear_output

from D21filter_and_visualize import order_data


def store_lower(val):
    clear_output()
    display(slider)
    temp = order_data.groupby('store_name')
    print(temp.size()[temp.size() < val['new']])


slider = IntSlider(value=1100, max=2000, step=100, description='件数:',)
slider.observe(store_lower, names='value')
display(slider)


def store_upper(val):
    clear_output()
    display(slider2)
    temp = order_data.groupby('store_name')
    print(temp.size()[temp.size() > val['new']])


slider2 = IntSlider(value=1600, min=1000, max=2000,
                    step=100, description='件数:',)
slider2.observe(store_upper, names='value')
display(slider2)

# %%
