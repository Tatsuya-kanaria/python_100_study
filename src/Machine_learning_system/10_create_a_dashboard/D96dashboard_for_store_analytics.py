# %%
import seaborn as sns
from IPython.display import display, clear_output
from ipywidgets import Select, SelectMultiple
import matplotlib.pyplot as plt
import japanize_matplotlib


from D91single_data_load import store_monthly_data


store_list = store_monthly_data['store_name'].unique()


def make_graph_96(val):
    clear_output()
    display(select_96)

    fig = plt.figure(figsize=(17, 4))
    plt.subplots_adjust(wspace=0.25, hspace=0.6)

    for i, trg in enumerate(val['new'], start=1):
        pick_data = store_monthly_data.loc[store_monthly_data['store_name'] == trg]

        graph_fin = pick_data[
            [
                'store_name',
                'order_fin',
                'year_month',
            ]
        ].copy()
        graph_fin['type'] = 'fin'
        graph_fin = graph_fin.rename(columns={'order_fin': 'count'})

        graph_cancel = pick_data[
            [
                'store_name',
                'order_cancel',
                'year_month',
            ]
        ].copy()
        graph_cancel['type'] = 'cancel'
        graph_cancel = graph_cancel.rename(columns={'order_cancel': 'count'})

        ax = fig.add_subplot(1, len(val['new']), i)
        sns.pointplot(
            x="year_month",
            y="count",
            data=graph_fin,
            color='orange'
        )

        sns.pointplot(
            x="year_month",
            y="count",
            data=graph_cancel,
            color='blue'
        )

        ax.set_title(trg)


select_96 = SelectMultiple(options=store_list)
select_96.observe(make_graph_96, names='value')

display(select_96)

# %%
