# %%
import pandas as pd

import D52split as D52


with open('./data/hashire_merosu.txt', mode='r', encoding='shift-jis') as f:
    content = f.readlines()
content

df = pd.DataFrame(content, columns=['text'])
df['text'] = df['text'].str.replace('\n', '')

title = df.iat[0, 0]
# print(title)
author = df.iat[1, 0]
# print(author)

date = df[(df['text'].str.contains('日公開')) | (
    df['text'].str.contains('日修正'))].copy()
# print(date)


date['text'] = date['text'].str.replace('公開', '')
date['text'] = date['text'].str.replace('修正', '')
# print(date)

# df_replace(date, 'text', "/", '年', '月', '日')
# date['text'] = date['text'].str.replace('年', '/')
# date['text'] = date['text'].str.replace('月', '/')
# date['text'] = date['text'].str.replace('日', '/')
# print(date)

date['text'] = pd.to_datetime(date['text'], format='%Y年%m月%d日')
# print(date)

# iat[行, 列]:
release_date = date.iat[0, 0]
update_date = date.iat[1, 0]
# print(release_date)
# print(update_date)
date = update_date - release_date
# print(date)

booklist = pd.DataFrame([[title, author, release_date, update_date, D52.body]], columns=[
                        'title',
                        'author',
                        'release_date',
                        'update_date',
                        'body'])

if __name__ == '__main__':
    booklist



# %%
