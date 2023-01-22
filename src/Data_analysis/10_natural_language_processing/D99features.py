# %%
import MeCab
import ipadic
import pandas as pd

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

# %%
