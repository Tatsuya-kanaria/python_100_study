# %%
import matplotlib.pyplot as plt

import D91read_csv as D91
import D92remove_unnecessary_string

D91.survey["length"] = D91.survey["comment"].str.len()
D91.survey.head()

%matplotlib inline

plt.hist(D91.survey["length"],)

# %%
