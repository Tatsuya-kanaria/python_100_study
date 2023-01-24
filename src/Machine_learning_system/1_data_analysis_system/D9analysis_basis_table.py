# %%
import os

import D8set_name as D8

current_dir = os.getcwd()
output_dir = os.path.join(current_dir, 'output_data')

os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, 'order_data.csv')
D8.order_data.to_csv(output_file, index=False)

# %%
