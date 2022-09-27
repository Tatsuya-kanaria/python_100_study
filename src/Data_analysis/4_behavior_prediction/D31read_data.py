# %%
import pandas as pd

uselog = pd.read_csv('./data/use_log.csv')
uselog.isnull().sum()

customer = pd.read_csv('./data/customer_join.csv')
customer.isnull().sum()

# %%
