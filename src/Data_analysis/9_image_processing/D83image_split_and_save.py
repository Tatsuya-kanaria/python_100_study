# %%
import cv2


cap = cv2.VideoCapture('./data/mov/mov01.avi')
num = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)
        filepath = "./snapshot/snapshot_" + str(num) + ".jpg"
        cv2.imwrite(filepath, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    num += 1
cap.release()
cv2.destroyAllWindows()

# %%
