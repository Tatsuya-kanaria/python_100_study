# %%
import unicodedata
import re


with open('./data/hashire_merosu.txt', mode='r', encoding='shift-jis') as f:
    content = f.read()

# ' 'で区切った文章を繋ぐ
content = ' '.join(content.split())

# 正規化
# NFKC(Normalization Form Compatibility Composition)
# 互換等価性に基づく分解後、正準等価性に基づいて再度合成
content = unicodedata.normalize('NFKC', content)

pattern = re.compile(r'^.+(#地から1字上げ].+#地から1字上げ]).*$')
# ['#地から1字上げ] ------------------------------------------------------- ', '[#地から1字上げ]']
replace_pattern = re.compile(r'\[?#地から1字上げ]\s?-*\s?')

body = re.match(pattern, content).group(1)
# body = body.replace(置き換えたい文字列, 置き換え後の文字列)
body = re.sub(replace_pattern, '', body)

if __name__ == '__main__':
    body
# %%
