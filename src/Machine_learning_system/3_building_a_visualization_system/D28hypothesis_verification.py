# %%
from IPython.display import display
import pandas as pd

from D26build_from_story import cancel_df
from D27reason_for_cancellation import order_all


temp_cancel = cancel_df.copy()
temp_delivery = order_all.loc[order_all['status'] == 2].groupby([('store_id')])[
    'delta'].mean()
check_df = pd.merge(temp_cancel, temp_delivery, on='store_id', how='left')
check_df.head()

temp_chk = check_df[['cancel_rate', 'delta']]
display(temp_chk.corr())

# キャンセル率が高い（第3四分位以上）店舗のみ
th_high = check_df['cancel_rate'].quantile(0.75)
temp_chk = check_df.loc[(check_df['cancel_rate'] >= th_high)]
temp_chk = temp_chk[['cancel_rate', 'delta']]
display(temp_chk.corr())

# キャンセル率が低い（第1四分位以上）店舗のみ
th_low = check_df['cancel_rate'].quantile(0.25)
temp_chk = check_df.loc[(check_df['cancel_rate'] >= th_low)]
temp_chk = temp_chk[['cancel_rate', 'delta']]
display(temp_chk.corr())

# %%
