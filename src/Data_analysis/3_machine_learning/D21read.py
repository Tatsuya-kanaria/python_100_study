# %%
import pandas as pd


uselog = pd.read_csv('./data/use_log.csv')
customer = pd.read_csv('./data/customer_master.csv')
class_master = pd.read_csv('./data/class_master.csv')
campaign_master = pd.read_csv('./data/campaign_master.csv')

if __name__ == '__main__':
    print("userlog: ", len(uselog))
    print("customer: ", len(customer))
    print("class_master: ", len(class_master))
    print("campaign_master: ", len(campaign_master))

uselog.head()
customer.head()
class_master.head()
campaign_master.head()

# %%
