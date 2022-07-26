# %%
import pandas as pd


# 先頭に数字があるためこの方法で読み込んだ
import D27melt2
import D28review


datas_v_all = pd.concat(
    [D27melt2.datas_v,  D28review.ca_datas_v], ignore_index=True)
# display(datas_v_all.head())
# display(datas_v_all.tail())

# 4月の発電所種別データの表示
pd.pivot_table(datas_v_all.loc[datas_v_all['年月'] == '2020.4'],
               index='発電所種別', columns='項目', values='値', aggfunc='sum')

# %%
