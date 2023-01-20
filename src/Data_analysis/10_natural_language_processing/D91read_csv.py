# %%
import pandas as pd


survey = pd.read_csv("./data/survey.csv")
if __name__ == "__main__":
    print(len(survey))

# 欠損値の除去
survey = survey.dropna()
survey.isna().sum()

survey.head()

# %%
