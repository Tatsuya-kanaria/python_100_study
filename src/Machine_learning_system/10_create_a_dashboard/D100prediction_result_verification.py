# %%
import seaborn as sns

from D95preprocessing_data_for_models import report_valid


view_data = report_valid.copy()
view_data.loc[
    (
        view_data['score_weekday'] >= 0.5
    ) & (
        view_data['y_weekday'] == 1
    ),
    'correct_weekday'
] = 1

view_data.loc[
    (
        view_data['score_weekday'] < 0.5
    ) & (
        view_data['y_weekday'] == 1
    ),
    'correct_weekday'
] = 1

view_data.loc[
    (
        view_data['score_weekend'] >= 0.5
    ) & (
        view_data['y_weekend'] == 1
    ),
    'correct_weekend'
] = 1

view_data.loc[
    (
        view_data['score_weekend'] < 0.5
    ) & (
        view_data['y_weekend'] == 1
    ),
    'correct_weekend'
] = 1

view_data['count'] = 1
view_data.fillna(0, inplace=True)
view_data = view_data.groupby('pred_year_month').sum(
)[
    [
        'correct_weekday',
        'correct_weekend',
        'count',
    ]
]

view_data['acc_weekday'] = view_data['correct_weekday'] / view_data['count']
view_data['acc_weekend'] = view_data['correct_weekend'] / view_data['count']

view_data = view_data[['acc_weekday', 'acc_weekend']]

sns.heatmap(view_data.T, cmap='Blues', annot=True,
            yticklabels=2, linewidths=.5)

# %%
