# %%

import D55mecab_dt as D55


mecab_df = D55.mecab_df

if __name__ == '__main__':
    print(mecab_df.groupby(['原形', '品詞']).size().sort_values(ascending=False))

noun = mecab_df.loc[mecab_df['品詞'] == '名詞']
# noun

verb = mecab_df.loc[(mecab_df['品詞'] == '名詞') | (mecab_df['品詞'] == '動詞')]
verb

# %%
