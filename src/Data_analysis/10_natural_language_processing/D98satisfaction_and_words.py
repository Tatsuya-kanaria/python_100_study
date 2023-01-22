# %%
import MeCab
import ipadic
import pandas as pd

import D91read_csv as D91
import D92remove_unnecessary_string


tagger = MeCab.Tagger(ipadic.MECAB_ARGS)

all_words = []
satisfaction = []
parts = ["名詞"]
stop_words = ["の"]

for n in range(len(D91.survey)):
    text = D91.survey["comment"].iloc[n]
    words = tagger.parse(text).splitlines()
    words_arr = []
    for i in words:
        if i == 'EOS' or i == '':
            continue
        word_temp = i.split()[0]
        part = i.split()[1].split(",")[0]
        if not (part in parts):
            continue
        if word_temp in stop_words:
            continue
        words_arr.append(word_temp)
        satisfaction.append(D91.survey["satisfaction"].iloc[n])
    all_words.extend(words_arr)

all_words_df = pd.DataFrame(
    {"words": all_words, "satisfaction": satisfaction, "count": len(all_words)*[1]})
all_words_df.head()

words_satisfaction = all_words_df.groupby("words").mean()["satisfaction"]
words_count = all_words_df.groupby("words").sum()["count"]
words_df = pd.concat([words_satisfaction, words_count], axis=1)
words_df.head()

words_df = words_df.loc[words_df["count"] >= 3]
words_df.sort_values("satisfaction", ascending=False).head()

words_df.sort_values("satisfaction").head()

# %%
