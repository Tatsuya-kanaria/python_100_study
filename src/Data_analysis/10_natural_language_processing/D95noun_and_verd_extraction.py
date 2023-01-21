# %%
import MeCab
import ipadic


tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
text = "すもももももももものうち"
words = tagger.parse(text).splitlines()

# print(words)
'''['すもも\t名詞,一般,*,*,*,*,すもも,スモモ,スモモ', 'も\t助詞,係助詞,*,*,*,*,も,モ,モ', 'もも\t名詞,一般,*,*,*,*,もも,モモ,モモ', 'も\t助詞,係助詞,*,*,*,*,も,モ,モ', 'もも\t名詞,一般,*,*,*,*,もも,モモ,モモ', 'の\t助詞,連体化,*,*,*,*,の,ノ,ノ', 'うち\t名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ', 'EOS']'''

words_arr = []
parts = ["名詞", "動詞"]
for i in words:
    if i == 'EOS' or i == '':
        continue
    word_temp = i.split()[0]
    part = i.split()[1].split(",")[0]
    if not (part in parts):
        continue
    words_arr.append(word_temp)

words_arr


# %%
