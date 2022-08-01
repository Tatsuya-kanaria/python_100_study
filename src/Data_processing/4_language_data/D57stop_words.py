# %%

import D56take_out as D56

# %%

with open('./data/stop_words.txt', mode='r') as f:
    stop_words = f.read().split()
# stop_words


# print(len(D56.noun))
# ~: 否定 .isin: 含んでいる場合 True
noun = D56.noun.loc[~D56.noun['原形'].isin(stop_words)]

# print(len(noun))
# print(noun.head())

# print(len(D56.verb))
verb = D56.verb.loc[~D56.verb['原形'].isin(stop_words)]

# print(len(verb))
# print(verb.head())


# %%
