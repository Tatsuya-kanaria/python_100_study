# %%
from moviepy.editor import VideoFileClip


video_clip = VideoFileClip('./data/sample_video.mp4')
video_clip.audio.write_audiofile('./data/audio_by_py.mp3')

# ffmpegを利用して変換する。
# ffmpeg -i ./data/sample_video.mp4 -y -hide_banner -loglevel error data/audio_by_ffmpeg.mp3

# %%
