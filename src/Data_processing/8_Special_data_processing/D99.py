# %%
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


df = pd.read_csv('./data/person_count_out_0001_2021011509.csv')
df.head()

fig = px.line(x=df['receive_time'], y=df['in1'])

df_v = pd.melt(df[['receive_time', 'in1', 'out1']], id_vars=[
               'receive_time'], var_name="変数名", value_name="値")
df_v.head()

fig = px.line(df_v, x='receive_time', y='値', color='変数名')

fig.show()

# %%
