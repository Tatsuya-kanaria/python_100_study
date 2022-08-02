# %%
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

import D57stop_words as D57

count = D57.verb.groupby('原形').size().sort_values(ascending=False)
count.name = 'count'
count = count.reset_index().head(10)
count

plt.figure(figsize=(10, 5))
sns.barplot(x=count['count'], y=count['原形'])

# %%
