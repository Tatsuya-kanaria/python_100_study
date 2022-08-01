# %%
import MeCab
# OSにMeCabインストールせずに使用する
import ipadic

import D53booklist as D53


tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
body = D53.booklist.iloc[0, 4]

parsed = tagger.parse(body).split('\n')
# 末尾2行削除
parsed = parsed[:-2]
parsed[-4:]

# %%
