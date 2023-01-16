# %%
import cv2


# 準備 #
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hogParams = {'winStride': (8, 8), 'padding': (
    32, 32), 'scale': 1.05, 'hitThreshold': 0, 'groupThreshold': 5}

# 検出 #
img = cv2.imread('./data/img/img01.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
human, r = hog.detectMultiScale(gray, **hogParams)
if (len(human) > 0):
    for (x, y, w, h) in human:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)
cv2.imshow('img', img)
cv2.waitKey(0)

# %%
