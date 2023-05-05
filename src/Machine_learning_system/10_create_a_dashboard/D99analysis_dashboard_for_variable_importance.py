# %%
import seaborn as sns
from IPython.display import display, clear_output
from ipywidgets import Select, SelectMultiple
import matplotlib.pyplot as plt
import japanize_matplotlib

# from D92created_by_reading_update_data import score_all
from D93important_variable_combination import importance_all

opt1 = ''
opt2 = ''


def update_option(option, value):
    global opt1, opt2

    if option == 's1':
        opt1 = value['new']
    elif option == 's2':
        opt2 = value['new']
    else:
        raise ValueError('Enter "s1" or "s2" in the first variable')

    if opt1 and opt2:
        graph_by_multi()


def graph_by_multi():
    clear_output()
    display(select1, select2)

    importance_tg_wd = importance_all.loc[
        (
            importance_all['model_name'] == opt1
        ) & (
            importance_all['year_month'] == opt2
        ) & (
            importance_all['model_target'] == 'y_weekday'
        )
    ].copy()

    importance_tg_we = importance_all.loc[
        (
            importance_all['model_name'] == opt1
        ) & (
            importance_all['year_month'] == opt2
        ) & (
            importance_all['model_target'] == 'y_weekend'
        )
    ].copy()

    importance_tg_wd.sort_values('importance', ascending=False, inplace=True)
    importance_tg_we.sort_values('importance', ascending=False, inplace=True)

    importance_tg_wd = importance_tg_wd.head(10)
    importance_tg_we = importance_tg_we.head(10)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    plt.subplots_adjust(wspace=0.25, hspace=0.6)

    ax1 = fig.add_subplot(1, 2, 1)
    plt.barh(importance_tg_wd['cols'], importance_tg_wd['importance'])
    ax1.set_title('平日')

    ax2 = fig.add_subplot(1, 2, 2)
    plt.barh(importance_tg_we['cols'], importance_tg_we['importance'])
    ax2.set_title('週末')


s1_option = importance_all['model_name'].unique()
s2_option = importance_all['year_month'].unique()

select1 = Select(options=s1_option)
select1.observe(lambda change: update_option('s1', change), names='value')

select2 = Select(options=s2_option)
select2.observe(lambda change: update_option('s2', change), names='value')

display(select1, select2)

# %%
