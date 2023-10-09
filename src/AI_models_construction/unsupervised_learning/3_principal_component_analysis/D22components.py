# %%
import seaborn as sns
import matplotlib.pyplot as plt

from D21PCA import pca


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
sns.heatmap(pca.components_,
            cmap="Blues",
            annot=True,
            annot_kws={"size": 14},
            fmt=".2f",
            xticklabels=["SepalLength", "SepalWidth",
                         "PetalLength", "PetalWidth"],
            yticklabels=["PC1", "PC2", "PC3", "PC4"],
            ax=ax)
plt.show()

# %%
