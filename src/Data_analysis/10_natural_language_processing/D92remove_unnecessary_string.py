# %%
import D91read_csv as D91


D91.survey["comment"] = D91.survey["comment"].str.replace("AA", "")

D91.survey["comment"] = D91.survey["comment"].str.replace(
    "[\（\(].+?[\）\)]", "", regex=True)

D91.survey["comment"].head()

# %%
