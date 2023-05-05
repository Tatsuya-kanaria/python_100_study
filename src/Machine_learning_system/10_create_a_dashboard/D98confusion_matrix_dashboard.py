# %%
import seaborn as sns
from IPython.display import display, clear_output
from ipywidgets import Select, SelectMultiple
import matplotlib.pyplot as plt
import japanize_matplotlib

from D92created_by_reading_update_data import score_all


opt1 = ''
opt2 = ''


# def s1_update_98(val):
#     global opt1
#     opt1 = val['new']
#     if empty_judgment():
#         graph_98()


# def s2_update_98(val):
#     global opt2
#     opt2 = val['new']
#     if empty_judgment():
#         graph_98()


# def empty_judgment():
#     global opt1
#     global opt2
#     return opt1 and opt2

# def graph_98():
#     clear_output()
#     display(select1_98, select2_98)

#     for i, ym in enumerate(score_all['year_month'].unique()):
#         fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
#         plt.subplots_adjust(wspace=0.25, hspace=0.6)

#         tmp = score_all.loc[
#             (
#                 score_all['model_name'] == opt1
#             ) & (
#                 score_all['model_target'] == opt2
#             ) & (
#                 score_all['DataCategory'] == 'train'
#             ) & (
#                 score_all['year_month'] == ym
#             )
#         ]

#         if len(tmp) == 1:
#             maxcnt = tmp["tp"].values[0] \
#                 + tmp["fn"].values[0] \
#                 + tmp["fp"].values[0] \
#                 + tmp["tn"].values[0]

#             cm = [
#                 [
#                     tmp["tp"].values[0]/maxcnt,
#                     tmp["fn"].values[0]/maxcnt
#                 ],
#                 [
#                     tmp["fp"].values[0]/maxcnt,
#                     tmp["tn"].values[0]/maxcnt,
#                 ]
#             ]
#             ax1 = fig.add_subplot(1, 2, 1)
#             sns.heatmap(
#                 cm,
#                 vmax=0.5,
#                 vmin=0,
#                 cmap='Blues',
#                 annot=True,
#                 xticklabels=False,
#                 yticklabels=False,
#                 cbar=False
#             )
#             ax1.set_title(f'{ym} train')

#         tmp = score_all.loc[
#             (
#                 score_all['model_name'] == opt1
#             ) & (
#                 score_all['model_target'] == opt2
#             ) & (
#                 score_all['DataCategory'] == 'test'
#             ) & (
#                 score_all['year_month'] == ym
#             )
#         ]

#         if len(tmp) == 1:
#             maxcnt = tmp["tp"].values[0] \
#                 + tmp["fn"].values[0] \
#                 + tmp["fp"].values[0] \
#                 + tmp["tn"].values[0]

#             cm = [
#                 [
#                     tmp["tp"].values[0]/maxcnt,
#                     tmp["fn"].values[0]/maxcnt
#                 ],
#                 [
#                     tmp["fp"].values[0]/maxcnt,
#                     tmp["tn"].values[0]/maxcnt,
#                 ]
#             ]
#             ax2 = fig.add_subplot(1, 2, 2)
#             sns.heatmap(
#                 cm,
#                 vmax=0.5,
#                 vmin=0,
#                 cmap='Blues',
#                 annot=True,
#                 xticklabels=False,
#                 yticklabels=False,
#                 cbar=False
#             )
#             ax2.set_title(f'{ym} test')

def update_option(option, value):
    global opt1, opt2

    if option == 's1':
        opt1 = value['new']
    elif option == 's2':
        opt2 = value['new']
    else:
        raise ValueError('Enter "s1" or "s2" in the first variable')

    if opt1 and opt2:
        plot_graph_98()


def plot_graph_98():
    clear_output()
    display(select1_98, select2_98)

    for ym in score_all['year_month'].unique():
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        plt.subplots_adjust(wspace=0.25, hspace=0.6)

        for i, (dc, ax) in enumerate(zip(['train', 'test'], [ax1, ax2]), start=1):

            tmp = score_all.loc[
                (
                    score_all['model_name'] == opt1
                ) & (
                    score_all['model_target'] == opt2
                ) & (
                    score_all['DataCategory'] == dc
                ) & (
                    score_all['year_month'] == ym
                )
            ]

            if len(tmp) == 1:
                maxcnt = tmp["tp"].values[0] \
                    + tmp["fn"].values[0] \
                    + tmp["fp"].values[0] \
                    + tmp["tn"].values[0]

                cm = [
                    [tmp["tp"].values[0]/maxcnt, tmp["fn"].values[0]/maxcnt],
                    [tmp["fp"].values[0]/maxcnt, tmp["tn"].values[0]/maxcnt,]
                ]
                ax = fig.add_subplot(1, 2, i)
                sns.heatmap(
                    cm,
                    vmax=0.5,
                    vmin=0,
                    cmap='Blues',
                    annot=True,
                    xticklabels=False,
                    yticklabels=False,
                    cbar=False
                )
                ax.set_title(f'{ym} {dc}')


s1_option_98 = score_all['model_name'].unique()
s2_option_98 = score_all['model_target'].unique()

select1_98 = Select(options=s1_option_98)
# select1_98.observe(s1_update_98, names='value')
select1_98.observe(lambda change: update_option('s1', change), names='value')

select2_98 = Select(options=s2_option_98)
# select2_98.observe(s2_update_98, names='value')
select2_98.observe(lambda change: update_option('s2', change), names='value')

display(select1_98, select2_98)

# %%
