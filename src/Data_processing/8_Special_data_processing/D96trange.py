# %%
import cv2
from tqdm import trange
import os


# 動画ファイルを分割して画像ファイルへ
cap = cv2.VideoCapture('./data/sample_video.mp4')
img_dir = './data/images_by_py'
# exist_ok すでに存在してもいいか
os.makedirs(img_dir, exist_ok=True)
n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

#  trange 進行状況を表示させる
for i in trange(n):
    success, img = cap.read()
    if not success:
        continue
    cv2.imwrite(f'{img_dir}/{i:04}.png', img)

# ffmpeg
# mkdir data/images_by_ffmpeg
# %04d 10進数値を0埋4桁で表示する
# ffmpeg -i ./data/sample_video.mp4 -y -hide_banner -loglevel error ./data/images_by_ffmpeg/%04d.png


# %%
