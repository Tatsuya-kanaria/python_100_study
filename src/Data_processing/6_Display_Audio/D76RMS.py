# %%

import librosa
import numpy as np
import matplotlib.pyplot as plt

audio1, sr1 = librosa.load('./data/音声.mp3', sr=None, offset=0, duration=1)

audio1_sr22, sr1_sr22 = librosa.load(
    './data/音声.mp3', sr=22050, offset=0, duration=1)

audio1_sr8 = librosa.resample(audio1, sr1, 8000)

audio2, sr2 = librosa.load('./data/携帯電話着信音.mp3', sr=None, offset=0, duration=1)

# RMS : root mean square 2乗して平均をとって平方根する

audio1_rms = np.sqrt(np.mean(audio1**2))
audio2_rms = np.sqrt(np.mean(audio2**2))
print(audio1_rms)
print(audio2_rms)

rms1 = librosa.feature.rms(y=audio1)
time1 = librosa.times_like(rms1, sr=sr1)
print(rms1.shape)

rms2 = librosa.feature.rms(y=audio2)
time2 = librosa.times_like(rms2, sr=sr2)
print(rms2.shape)

plt.plot(time1, rms1[0], label="audio1")
plt.plot(time2, rms2[0], label="audio2")
plt.legend()

# %%
