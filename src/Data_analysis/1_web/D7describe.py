# %%
import D5create_column as D5
from D4merge2 import join_data

# 欠損値の確認
join_data.isnull().sum()

# 統計値の表示
join_data.describe()

if __name__ == '__main__':
    print(join_data['payment_date'].min())
    print(join_data['payment_date'].max())

# %%
