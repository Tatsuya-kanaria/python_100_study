# %%

import IPython.display as disp
import librosa

audio1, sr1 = librosa.load('./data/音声.mp3', sr=None, offset=0, duration=1)

audio1_sr22, sr1_sr22 = librosa.load(
    './data/音声.mp3', sr=22050, offset=0, duration=1)
print(audio1_sr22)
print(sr1_sr22)

print(audio1_sr22.shape)

audio1_sr8 = librosa.resample(audio1, sr1, 8000)
print(audio1_sr8)
print(audio1_sr8.shape)

librosa.get_samplerate('./data/音声.mp3')


# %%
