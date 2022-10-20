# %%
import networkx as nx

import D53network_visualization as D53


D53.G.add_node("nodeD")

D53.G.add_edge("nodeA", "nodeD")

D53.pos["nodeD"] = (1, 0)

nx.draw(D53.G, D53.pos, with_labels=True)

# %%
