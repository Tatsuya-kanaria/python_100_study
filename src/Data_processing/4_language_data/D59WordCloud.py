# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import japanize_matplotlib

import D57stop_words as D57


font_path = '~/Library/Fonts/SourceHanCodeJP.ttc'
# "[\w']+": 1文字以上
cloud = WordCloud(background_color='white', font_path=font_path, regexp=r"[\w']{2,}").generate(
    ' '.join(D57.noun['原形'].values))

plt.figure(figsize=(10, 5))
plt.imshow(cloud)
# 軸
plt.axis("off")
# 保存
plt.savefig('./data/wc_noun_base_2.png')
plt.show()


# %%
