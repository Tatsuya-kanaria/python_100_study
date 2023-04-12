# %%
import os
import pickle

from D71folder_generation import model_dir


# model_weekday_name = 'model_y_weekday_GradientBoosting.pickle'
# model_weekend_name = 'model_y_weekend_GradientBoosting.pickle'

# model_weekday_path = os.path.join(model_dir, model_weekday_name)
# model_weekend_path = os.path.join(model_dir, model_weekend_name)

# with open(model_weekend_path, mode='rb') as f:
#     model_weekday = pickle.load(f)

# with open(model_weekend_path, mode='rb') as f:
#     model_weekend = pickle.load(f)

# print(model_weekday)
# print(model_weekend)

model_name = [
    'model_y_weekday_GradientBoosting.pickle',
    'model_y_weekend_GradientBoosting.pickle'
]

models = []
for name in model_name:
    path = os.path.join(model_dir, name)
    with open(path, mode='rb') as f:
        model = pickle.load(f)
        models.append(model)

model_weekday, model_weekend = models
print(model_weekday)
print(model_weekend)

# %%
