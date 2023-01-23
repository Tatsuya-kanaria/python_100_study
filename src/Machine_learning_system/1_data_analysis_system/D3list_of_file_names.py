# %%
import os
import glob


current_dir = os.getcwd()
current_dir

os.listdir(current_dir)

tbl_order_file = os.path.join(current_dir, './data/tbl_order_*.csv')
tbl_order_file

tbl_order_files = glob.glob(tbl_order_file)
tbl_order_files

# %%
