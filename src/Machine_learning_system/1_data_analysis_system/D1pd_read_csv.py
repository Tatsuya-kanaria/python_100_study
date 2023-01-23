# %%
import pandas as pd


m_store = pd.read_csv('./data/m_store.csv')
m_area = pd.read_csv('./data/m_area.csv')
tbl_order_4 = pd.read_csv('./data/tbl_order_202004.csv')

if __name__ == '__main__':
    print(m_store, m_area, tbl_order_4)

# %%
