# %%
import pandas as pd

from D64build_one_model import model, X_train


importance = pd.DataFrame(
    {'cols': X_train.columns, 'importance': model.feature_importances_})
importance = importance.sort_values('importance', ascending=False)
importance.head(10)

# %%
