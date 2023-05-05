# %%
from sklearn.metrics import accuracy_score
from sklearn.metrics import adjusted_rand_score

from D1k_means_non_hierarchical import iris, cls_data


ari = "ARI: {:.2f}".format(adjusted_rand_score(
    iris.target, cls_data["cluster"]))

accuracy = "Accuracy: {:.2f}".format(
    accuracy_score(iris.target, cls_data["cluster"]))

print(ari, accuracy, sep='\n')

# %%
