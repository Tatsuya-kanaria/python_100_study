# %%
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('./data/sample.jpg')
# plt.imshow(img)

height, width, channels = img.shape
print(height, width)

img_resized = cv2.resize(img, (500, 300))

# x軸とy軸を1/10にする
img_resized = cv2.resize(img, None, fx=0.1, fy=0.1)
print(img_resized.shape)
plt.imshow(img_resized)

img_rotated = cv2.rotate(img_resized, cv2.ROTATE_90_CLOCKWISE)
plt.imshow(img_rotated)
print("ROTATE_90_CLOCKWISE: ", img_rotated.shape)

# 中心を起点にして45°回転
height, width = img_resized.shape[:2]
center = (int(width/2), int(height/2))

rot = cv2.getRotationMatrix2D(center, 45, 1)
img_rotated = cv2.warpAffine(img_resized, rot, (width, height))
plt.imshow(img_rotated)
print("getRotationMatrix2D: ", img_rotated.shape)

# 上下反転
# flip 第2引数 0より大きい:左右反転 0:上下反転 0より小さい:上下左右反転
img_reverse = cv2.flip(img_resized, -1)
plt.imshow(img_reverse)
print("flip: ", img_reverse.shape)

# 配列の入れ替えによる左右反転
img_reverse = img_resized[:, ::-1, :]
plt.imshow(img_reverse)
print("flip: ", img_reverse.shape)


# %%
