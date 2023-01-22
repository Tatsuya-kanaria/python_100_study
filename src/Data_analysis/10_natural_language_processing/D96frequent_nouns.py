# %%
import MeCab
import ipadic
import pandas as pd

import D91read_csv as D91
import D92remove_unnecessary_string


tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
all_words = []
parts = ["名詞"]

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
        words_arr.append(word_temp)
    all_words.extend(words_arr)

print(all_words)

all_words_df = pd.DataFrame({"words": all_words, "count": len(all_words)*[1]})
all_words_df = all_words_df.groupby("words").sum()
all_words_df.sort_values("count", ascending=False).head(10)

# %%
