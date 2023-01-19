# %%
import cv2
import pandas as pd
import matplotlib.pyplot as plt

print("分析を開始します")
# 映像取得 #
cap = cv2.VideoCapture("./data/mov/mov01.avi")
fps = cap.get(cv2.CAP_PROP_FPS)

# hog宣言 #
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hogParams = {'winStride': (8, 8), 'padding': (
    32, 32), 'scale': 1.05, 'hitThreshold': 0, 'groupThreshold': 5}

num = 0
list_df2 = pd.DataFrame(columns=['time', 'people'])
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        if (num % 10 == 0):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            human, r = hog.detectMultiScale(gray, **hogParams)
            if (len(human) > 0):
                for (x, y, w, h) in human:
                    cv2.rectangle(frame, (x, y), (x + w, y + h),
                                  (255, 255, 255), 3)
            tmp_se = pd.Series([num/fps, len(human)], index=list_df2.columns)
            list_df2 = list_df2.append(tmp_se, ignore_index=True)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        break
    num = num + 1
cap.release()
cv2.destroyAllWindows()
print("分析を終了しました")

plt.plot(list_df2["time"], list_df2["people"])
plt.xlabel('time(sec.)')
plt.ylabel('population')
plt.ylim(0, 15)
plt.show()

# %%
