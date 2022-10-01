# %%
import D38predict_model_create as D38

import pandas as pd

coef = pd.DataFrame({"feature_names": D38.X.columns,
                    "coefficient": D38.model.coef_})

coef
# %%
