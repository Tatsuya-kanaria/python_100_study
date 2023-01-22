# %%
import MeCab
import ipadic
import pandas as pd
import numpy as np

import D91read_csv as D91
import D92remove_unnecessary_string


tagger = MeCab.Tagger(ipadic.MECAB_ARGS)


parts = ["名詞"]
all_words_df = pd.DataFrame()
satisfaction = []

for n in range(len(D91.survey)):
    text = D91.survey["comment"].iloc[n]
    words = tagger.parse(text).splitlines()
    words_df = pd.DataFrame()
    for i in words:
        if i == 'EOS' or i == '':
            continue
        word_temp = i.split()[0]
        part = i.split()[1].split(",")[0]
        if not (part in parts):
            continue
        words_df[word_temp] = [1]
    all_words_df = pd.concat([all_words_df, words_df], ignore_index=True)
all_words_df.head()

all_words_df = all_words_df.fillna(0)
all_words_df.head()

print(D91.survey["comment"].iloc[2])
target_text = all_words_df.iloc[2]
print(target_text)

cos_sim = []
for i in range(len(all_words_df)):
    cos_text = all_words_df.iloc[i]
    cos = np.dot(target_text, cos_text) / \
        (np.linalg.norm(target_text) * np.linalg.norm(cos_text))
    cos_sim.append(cos)
all_words_df["cos_sim"] = cos_sim
all_words_df.sort_values("cos_sim", ascending=False).head()

for i in [2, 24, 15, 33, 50]:
    print(D91.survey["comment"].iloc[i])

# %%
