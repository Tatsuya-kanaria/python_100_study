# %%
import cv2
import matplotlib.pyplot as plt
from pandas import test


img = cv2.imread('./data/sample.jpg')
# plt.imshow(img)

# RGB変換
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# x軸とy軸を1/10にする
img_resized = cv2.resize(img, None, fx=0.1, fy=0.1)
print(img_resized.shape)
plt.imshow(img_resized)

# 文字を画像に表示
text = "9"
xy = (200, 110)
font = cv2.FONT_HERSHEY_COMPLEX
font_scale = 2
color = (255, 0, 0)
thickness = 2

img_text = cv2.putText(img_resized.copy(), text, xy,
                       font, font_scale, color, thickness)
plt.imshow(img_text)

# 短形を描画
x0, y0 = 200, 70
x1, y1 = 350, 330
color = (255, 0, 0)
thickness = 3

img_rect = cv2.rectangle(img_resized.copy(), (x0, y0),
                         (x1, y1), color, thickness)
plt.imshow(img_rect)

# %%
