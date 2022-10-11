# %%
import pandas as pd


factories = pd.read_csv("./data/tbl_factory.csv", index_col=0)
factories

warehouses = pd.read_csv("./data/tbl_warehouse.csv", index_col=0)
warehouses

cost = pd.read_csv("./data/rel_cost.csv", index_col=0)
cost

trans = pd.read_csv("./data/tbl_transaction.csv", index_col=0)
trans

join_data = pd.merge(trans, cost, left_on=["ToFC", "FromWH"], right_on=[
                     "FCID", "WHID"], how="left")

join_data = pd.merge(join_data, factories, left_on=[
                     "ToFC"], right_on=["FCID"], how="left")

join_data = pd.merge(join_data, warehouses, left_on=[
                     "FromWH"], right_on=["WHID"], how="left")

join_data = join_data[["TransactionDate", "Quantity", "Cost", "ToFC",
                       "FCName", "FCDemand", "FromWH", "WHName", "WHSupply", "WHRegion"]]

join_data.head()

kanto = join_data.loc[join_data["WHRegion"] == "関東"]
kanto.head()

tohoku = join_data.loc[join_data["WHRegion"] == "東北"]
tohoku.head()

# %%
