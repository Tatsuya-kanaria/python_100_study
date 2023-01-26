# %%
import D11read_csv as D11
import warnings
import sys

# 警告を表示しない
if not sys.warnoptions:
    warnings.simplefilter('ignore')

D11.analyze_data.describe()

D11.analyze_data.dtypes

D11.analyze_data[['store_id', 'coupon_cd']
                 ] = D11.analyze_data[['store_id', 'coupon_cd']].astype(str)

D11.analyze_data.dtypes

# %%
