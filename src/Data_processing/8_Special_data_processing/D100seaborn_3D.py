# %%
import seaborn as sns
import plotly.express as px


df_iris = sns.load_dataset('iris')
df_iris.head()

# 2次元
fig = px.scatter(df_iris, x='sepal_length', y='sepal_width', color='species')

fig.show()

fig3D = px.scatter_3d(df_iris, x='sepal_length',
                      y='sepal_width', z='petal_width', color='species')

fig3D.show()

# %%
