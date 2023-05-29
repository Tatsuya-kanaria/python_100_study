# %%
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn import cluster, preprocessing


X, y = make_blobs(
    n_samples=150,   # サンプルの点の総数
    n_features=2,    # 説明変数（次元数）の指定 default:2
    centers=3,       # クラスタの個数
    cluster_std=0.5,  # クラスタ内の標準偏差
    shuffle=True,    # サンプルをシャッフル
    random_state=0
)  # 乱数生成器の状態を指定
sc = preprocessing.StandardScaler()
X_norm = sc.fit_transform(X)
x = X_norm[:, 0]
y = X_norm[:, 1]

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(3, 1, 1)
ax1.scatter(x, y)

distortions = []
for i in range(1, 11):
    km = KMeans(
        n_clusters=i,
        n_init=10,
        max_iter=300,
        random_state=0
    )
    km.fit(X)
    distortions.append(km.inertia_)

ax2 = fig.add_subplot(3, 1, 2)
ax2.plot(range(1, 11), distortions, marker="o")
plt.xticks(range(1, 11))
ax2.set_xlabel("Number of clusters")
ax2.set_ylabel("Distortion")

km = KMeans(
    n_clusters=3,
    n_init=10,
    max_iter=300,
    random_state=0
)
z_km = km.fit(X_norm)
ax3 = fig.add_subplot(3, 1, 3)
ax3.scatter(x, y, c=z_km.labels_)
ax3.scatter(z_km.cluster_centers_[:, 0], z_km.cluster_centers_[
            :, 1], s=250, marker="*", c="red")

plt.show

# %%
