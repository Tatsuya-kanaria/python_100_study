# %%
import os
import pandas as pd


data_dir = 'data'
input_dir = os.path.join(data_dir, '0_input')
output_dir = os.path.join(data_dir, '1_output')
master_dir = os.path.join(data_dir, '99_master')
model_dir = 'models'

dirs = [input_dir, output_dir, master_dir, model_dir]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# %%
