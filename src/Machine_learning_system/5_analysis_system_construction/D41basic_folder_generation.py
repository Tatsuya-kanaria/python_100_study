# %%
import os


data_dir = "data"
input_dir = os.path.join(data_dir, "0_input")
output_dir = os.path.join(data_dir, "10_output")
master_dir = os.path.join(data_dir, "99_master")

# print(input_dir)

os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)
os.makedirs(master_dir, exist_ok=True)

# %%
