# %%
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('./data/sample.jpg')
# plt.imshow(img)
#                     高さ,  幅,  BRG
img_extract = img[700:1200, 300:800, :]

plt.imshow(img_extract[:, :, 1])
# %%
