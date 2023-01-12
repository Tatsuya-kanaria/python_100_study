# %%
import cv2


img = cv2.imread('./data/img/img01.jpg')
height, width = img.shape[:2]
print("画像幅: " + str(width))
print("画像高さ: " + str(height))
cv2.imshow("img", img)
print("press any key to exit")
cv2.waitKey(0)

# %%
