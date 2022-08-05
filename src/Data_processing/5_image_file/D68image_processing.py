# %%
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('./data/sample.jpg')
# plt.imshow(img)

# RGB変換
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# x軸とy軸を1/10にする
img_resized = cv2.resize(img, None, fx=0.1, fy=0.1)
print(img_resized.shape)
plt.imshow(img_resized)

img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray)
print("cvtColor", img_gray.shape)

# 二値化
th, img_th = cv2.threshold(img_gray, 60, 255, cv2.THRESH_BINARY)
plt.imshow(img_th)
print("threshold", img_th.shape)
print(th)

# ぼかし
img_smoothed = cv2.blur(img_resized, (8, 8))
plt.imshow(img_smoothed)
print(img_smoothed.shape)

# %%
