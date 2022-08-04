# %%
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('./data/sample.jpg')
# plt.imshow(img)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_rgb.shape

plt.imshow(img_rgb)
# 青が赤く発色される
plt.imshow(img)

# %%
