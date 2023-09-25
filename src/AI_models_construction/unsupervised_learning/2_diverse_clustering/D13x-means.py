# %%
import numpy as np
import matplotlib.pyplot as plt

from init import x, y, z_xm, xm_i


# x-means
plt.figure(figsize=(10, 3))
plt.scatter(x, y, c=z_xm)
centers = np.array(xm_i._xmeans__centers)
plt.scatter(centers[:, 0], centers[:, 1], s=250, marker="*", c="red")
plt.show

# %%
