# %%
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

import D56take_out as D56

count = D56.noun.groupby('原形').size().sort_values(ascending=False)
count.name = 'count'
count = count.reset_index().head(10)
count

plt.figure(figsize=(10, 5))
sns.barplot(x=count['count'], y=count['原形'])

# %%
