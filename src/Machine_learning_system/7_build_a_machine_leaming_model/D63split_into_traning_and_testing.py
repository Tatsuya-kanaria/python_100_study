# %%
from sklearn.model_selection import train_test_split

from D62supports_categorical_variables import ml_data

train_data, test_data = train_test_split(
    ml_data, test_size=0.3, random_state=0)

week_flags = ['Weekday', 'Weekend']
data_flags = ['Train', 'Test']

print(f'Train:{len(train_data)}件/ test:{len(test_data)}件')

for week_flg in week_flags:
    for data_flg in data_flags:
        if data_flg == 'Train':
            data = train_data
        elif data_flg == 'Test':
            data = test_data
        else:
            data = None

        for y_num in range(2):
            print(
                f'{week_flg} {data_flg}{y_num}:{len(data.loc[data["y_weekday"]==y_num])}件')

# print(f'Weekday Train0:{len(train_data.loc[train_data["y_weekday"]==0])}件')

# %%
