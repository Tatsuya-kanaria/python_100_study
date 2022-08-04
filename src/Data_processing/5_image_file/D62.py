# %%
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('./data/sample.jpg')

# plt.imshow(img)

print(img[0])
print(img[0].shape)

print(img[:, 0])
print(img[:, 0].shape)

print(img[:, :, 0])
print(img[:, :, 0].shape)


# %%
