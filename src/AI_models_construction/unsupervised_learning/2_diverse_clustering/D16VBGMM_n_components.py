# %%
import matplotlib.pyplot as plt
import numpy as np
from sklearn import mixture

from init import vbgmm, X_norm, x, y

# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
x_tick = np.arange(1, 11)

plt.figure(figsize=(10, 2))
plt.bar(x_tick, vbgmm.weights_, width=0.7, tick_label=x_tick)
plt.suptitle('VBGMM_weights')
plt.show

# 最適なクラスタ数に調整
vbgmm = mixture.BayesianGaussianMixture(n_components=3, random_state=0)
vbgmm = vbgmm.fit(X_norm)
labels = vbgmm.predict(X_norm)

plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=labels)
plt.suptitle("vbgmm")
plt.show

x_tick = np.arange(1, 4)
plt.figure(figsize=(10, 2))
plt.bar(x_tick, vbgmm.weights_, width=0.7, tick_label=x_tick)
plt.suptitle("vbgmm_weights")
plt.show

# %%
