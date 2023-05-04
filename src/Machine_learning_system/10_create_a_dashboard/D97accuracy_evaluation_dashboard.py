# %%
import seaborn as sns
from IPython.display import display, clear_output
from ipywidgets import Select, SelectMultiple
import matplotlib.pyplot as plt
import japanize_matplotlib

from D92created_by_reading_update_data import score_all


opt1 = ''


def s1_update_97(val):
    global opt1
    opt1 = val['new']
    graph_97()


def graph_97():
    clear_output()
    display(select1_97)

    graph_df_wd = score_all.loc[
        (
            score_all['model_name'] == opt1
        ) & (
            score_all['model_target'] == 'y_weekday'
        ).copy()
    ]

    graph_df_we = score_all.loc[
        (
            score_all['model_name'] == opt1
        ) & (
            score_all['model_target'] == 'y_weekend'
        ).copy()
    ]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    plt.subplots_adjust(wspace=0.25, hspace=0.6)

    ax1 = fig.add_subplot(1, 2, 1)
    sns.barplot(x='dirs', y='acc', data=graph_df_wd, hue='DataCategory')
    ax1.set_title('平日')

    ax2 = fig.add_subplot(1, 2, 2)
    sns.barplot(x='dirs', y='acc', data=graph_df_we, hue='DataCategory')
    ax2.set_title('休日')


s1_option_97 = score_all['model_name'].unique()

select1_97 = Select(options=s1_option_97)
select1_97.observe(s1_update_97, names='value')

display(select1_97)

# %%
