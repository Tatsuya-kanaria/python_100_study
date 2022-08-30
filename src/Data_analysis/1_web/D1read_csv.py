# %%
import pandas as pd


# マスターデータ読み込み
customer_master = pd.read_csv('./data/customer_master.csv')
# customer_master.head()

item_master = pd.read_csv('./data/item_master.csv')
# item_master.head()

transaction_1 = pd.read_csv('./data/transaction_1.csv')
# transaction_1.head()

transaction_detail_1 = pd.read_csv('./data/transaction_detail_1.csv')
# transaction_detail_1.head()

# %%
