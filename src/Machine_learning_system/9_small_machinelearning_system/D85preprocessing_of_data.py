# %%
import pandas as pd
from sklearn.model_selection import train_test_split

from D84update_ml_base_data import ml_base_data

category_data = pd.get_dummies(
    ml_base_data['store_name'], prefix='store', prefix_sep='_')

category_data.drop(columns=['store_麻生店'], inplace=True)
ml_base_data.drop(columns=['year_month', 'store_name'], inplace=True)

ml_base_data = pd.concat([ml_base_data, category_data], axis=1)

train_data, test_data = train_test_split(
    ml_base_data, test_size=0.3, random_state=0)


def print_split_data_info(train_data, test_data, target_col):
    print(
        f'Train : {len(train_data)}件 / Test : {len(test_data)}')
    print(
        f'{target_col} Train0 : {len(train_data.loc[train_data[target_col]==0])}件')
    print(
        f'{target_col} Train1 : {len(train_data.loc[train_data[target_col]==1])}件')
    print(
        f'{target_col} Test0 : {len(test_data.loc[test_data[target_col]==0])}件')
    print(
        f'{target_col} Test1 : {len(test_data.loc[test_data[target_col]==1])}件')


print_split_data_info(train_data, test_data, "y_weekday")
print_split_data_info(train_data, test_data, "y_weekend")


# %%
