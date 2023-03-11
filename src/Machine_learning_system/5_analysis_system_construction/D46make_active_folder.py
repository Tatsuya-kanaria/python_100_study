# %%
from D41basic_folder_generation import output_dir
from D42check_mechanism import tg_ym

import os
import datetime


def make_active_folder(targetYM):
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    target_output_dir_name = targetYM + "_" + now
    target_output_dir = os.path.join(output_dir, target_output_dir_name)
    os.makedirs(target_output_dir)
    print(target_output_dir_name)
    return target_output_dir


target_output_dir = make_active_folder(tg_ym)

# %%
