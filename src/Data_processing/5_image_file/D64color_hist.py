# %%
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('./data/sample.jpg')
# plt.imshow(img)
#                     高さ,  幅,  BRG
img_extract = img[700:1200, 300:800, :]

hist_b = cv2.calcHist([img],
                      channels=[0],
                      mask=None,
                      histSize=[256],
                      ranges=[0, 256])

print(hist_b.shape)
hist_b[:5]

hist_g = cv2.calcHist([img],
                      channels=[1],
                      mask=None,
                      histSize=[256],
                      ranges=[0, 256])

hist_r = cv2.calcHist([img],
                      channels=[2],
                      mask=None,
                      histSize=[256],
                      ranges=[0, 256])

plt.plot(hist_r, color='r', label="Red")
plt.plot(hist_g, color='g', label="Green")
plt.plot(hist_b, color='b', label="Blue")

# 凡例
plt.legend()
plt.title("color")
plt.show()

# %%
