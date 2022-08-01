# %%
import MeCab
# OSにMeCabインストールせずに使用する
import ipadic
import re
import pandas as pd

import D53booklist as D53


tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
body = D53.booklist.iloc[0, 4]

parsed = tagger.parse(body).split('\n')
# 末尾2行削除
parsed = parsed[:-2]

# \tと','で区切って配列に変換
*values, = map(lambda s: re.split(r'\t|,', s), parsed)
values[:4]

columns = ['表層形', '品詞', '品詞細分類1', '品詞細分類2',
           '品詞細分類3', '活用型', '活用形', '原形', '読み', '発音']

mecab_df = pd.DataFrame(data=values, columns=columns)
print(len(mecab_df))
mecab_df.head(4)

# %%
