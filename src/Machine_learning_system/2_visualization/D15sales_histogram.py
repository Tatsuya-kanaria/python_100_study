# %%
import D13sales_by_month as D13

import matplotlib.pyplot as plt
%matplotlib inline

plt.hist(D13.analyze_data['total_amount'])

plt.hist(D13.analyze_data['total_amount'], bins=21)

# %%
