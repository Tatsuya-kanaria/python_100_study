# %%
import numpy as np

import D76real_data as D76


NUM = len(D76.df_mem_info.index)
T_NUM = len(D76.df_mem_info.columns) - 1
# 消滅の確率推定
count_active = 0
count_active_to_inactive = 0
for t in range(1, T_NUM):
    for i in range(NUM):
        if (D76.df_mem_info.iloc[i][t] == 1):
            count_active_to_inactive += 1
            if (D76.df_mem_info.iloc[i][t+1] == 0):
                count_active += 1
estimated_percent_disapparence = count_active / count_active_to_inactive

# 拡散の確率推定
count_link = 0
count_link_to_active = 0
count_link_temp = 0
for t in range(T_NUM - 1):
    df_link_t = D76.df_mem_info[D76.df_mem_info[str(t)] == 1]
    temp_flag_count = np.zeros(NUM)
    for i in range(len(df_link_t.index)):
        df_link_temp = D76.df_mem_links[D76.df_mem_links["Node" +
                                                         str(df_link_t.index[i])] == 1]
        for j in range(len(df_link_temp.index)):
            if (D76.df_mem_info.iloc[df_link_temp.index[j]][str(t)] == 0):
                if (temp_flag_count[df_link_temp.index[j]] == 0):
                    count_link += 1
            if (D76.df_mem_info.iloc[df_link_temp.index[j]][str(t + 1)] == 0):
                if (temp_flag_count[df_link_temp.index[j]] == 0):
                    temp_flag_count[df_link_temp.index[j]] = 1
                    count_link_to_active += 1
estimated_percent_percolation = count_link_to_active / count_link


if __name__ == '__main__':
    print(estimated_percent_disapparence)
    print(estimated_percent_percolation)

# %%
