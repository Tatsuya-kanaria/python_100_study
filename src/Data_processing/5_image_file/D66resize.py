# %%
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('./data/sample.jpg')
# plt.imshow(img)

height, width, channels = img.shape
print(width, height)

img_resized = cv2.resize(img, (500, 300))

print(img_resized.shape)
plt.imshow(img_resized)

# 横300、縦500
img_resized = cv2.resize(img, (300, 500))
print(img_resized.shape)
plt.imshow(img_resized)

# x軸とy軸を1/10にする
img_resized = cv2.resize(img, None, fx=0.1, fy=0.1)
print(img_resized.shape)
plt.imshow(img_resized)

img_resized_2 = cv2.resize(img_resized, None, fx=1.5, fy=1.5)
print(img_resized_2.shape)
plt.imshow(img_resized_2)

# INTER_NEAREST法　新しい色は作らないが荒くなる
img_resized_2 = cv2.resize(img, None, fx=1.5, fy=1.5,
                           interpolation=cv2.INTER_NEAREST)
print(img_resized_2.shape)
plt.imshow(img_resized_2)


# %%
