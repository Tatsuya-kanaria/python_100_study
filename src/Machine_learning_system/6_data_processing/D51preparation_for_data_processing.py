# %%
import os
import glob


data_dir = 'data'
input_dir = os.path.join(data_dir, '0_input')
output_dir = os.path.join(data_dir, '1_output')
master_dir = os.path.join(data_dir, '99_master')
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)
os.makedirs(master_dir, exist_ok=True)

tbl_order_file = os.path.join(input_dir, 'tbl_order_*.csv')
tbl_order_paths = glob.glob(tbl_order_file)
tbl_order_paths

# %%
