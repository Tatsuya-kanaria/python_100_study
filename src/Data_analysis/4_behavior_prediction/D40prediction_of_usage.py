# %%
import D36forecast_preparation as D36
import D38predict_model_create as D38


x1 = [3, 4, 4, 7, 8, 7, 8]
x2 = [2, 2, 3, 3, 4, 6, 8]
x3 = [8, 7, 6, 6, 7, 4, 8]

x_pred = [x1, x2, x3]

D38.model.predict(x_pred)

D36.uselog_months.to_csv("./data/use_log_months.csv", index=False)

# %%
