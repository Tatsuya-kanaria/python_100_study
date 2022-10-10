# %%
import D48model_tuning as D48

import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

model = DecisionTreeClassifier(random_state=0, max_depth=5)
model.fit(D48.X_train, D48.y_train)

plt.figure(figsize=(15, 10))
plot_tree(model, filled=True)
plt.show()

# %%
