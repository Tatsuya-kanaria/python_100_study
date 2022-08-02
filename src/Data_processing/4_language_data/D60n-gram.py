# %%
from nltk import ngrams
import collections

import D55mecab_dt as D55


target = D55.mecab_df['表層形'].to_list()
len(target)

bigram = ngrams(target, 2)

counter = collections.Counter(bigram)
if __name__ == '__main__':
    print(counter)

# %%
