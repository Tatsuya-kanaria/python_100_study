# %%
import MeCab
import ipadic


tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
text = "すもももももももものうち"
words = tagger.parse(text)
words

words = tagger.parse(text).splitlines()
words_arr = []
for i in words:
    if i == 'EOS':
        continue
    word_temp = i.split()[0]
    words_arr.append(word_temp)

words_arr

# %%
