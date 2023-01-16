# %%
import cv2


# 準備
cascade_file = "./data/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

# 検出
img = cv2.imread("./data/img/img02.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_list = cascade.detectMultiScale(gray, minSize=(50, 50))

# 検出した顔に印を付ける
for (x, y, w, h) in face_list:
    color = (0, 0, 255)
    pen_w = 3
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness=pen_w)

cv2.imshow("img", img)
cv2.imwrite("temp.jpg", img)
cv2.waitKey(0)

# %%
