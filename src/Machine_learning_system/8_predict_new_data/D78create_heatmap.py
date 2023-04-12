# %%
import seaborn as sns
import japanize_matplotlib

from D77predict import pred


pred_viz = pred[['store_name', 'score_weekday', 'score_weekend']]
pred_viz.set_index('store_name', inplace=True)

pred_viz

japanize_matplotlib.japanize()
sns.heatmap(pred_viz[:20].T)

# %%
