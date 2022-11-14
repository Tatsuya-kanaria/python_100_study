# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


# データの読み込み
df_w = pd.read_csv('./data/network_weight.csv')
df_p = pd.read_csv('./data/network_pos.csv')

# エッジの重みのリスト化
size = 10
edge_weights = []
for i in range(len(df_w)):
    for j in range(len(df_w.columns)):
        edge_weights.append(df_w.iloc[i][j] * size)

# グラフオブジェクトの作成
G = nx.Graph()

# 頂点の設定
for i in range(len(df_w.columns)):
    G.add_node(df_w.columns[i])

# 辺の設定
for i in range(len(df_w.columns)):
    for j in range(len(df_w.columns)):
        G.add_edge(df_w.columns[i], df_w.columns[j])

# 座標の設定
pos = {}
for i in range(len(df_w.columns)):
    node = df_w.columns[i]
    pos[node] = (df_p[node][0], df_p[node][1])

# 描画
nx.draw(G, pos, with_labels=True, font_size=16, node_size=1000,
        node_color='k', font_color='w', width=edge_weights)

plt.show()
# %%
