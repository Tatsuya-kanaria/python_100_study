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

rms1 = librosa.feature.rms(y=audio1)
time1 = librosa.times_like(rms1, sr=sr1)

rms2 = librosa.feature.rms(y=audio2)
time2 = librosa.times_like(rms2, sr=sr2)

# 周波数触幅スペクトル
# audio1, audio2, audio1_sr22
fft = np.fft.fft(audio2)
n = fft.size
amp = np.abs(fft)
freq = np.fft.fftfreq(n, d=1 / sr2)

print(amp.shape)
print(freq.shape)
print(amp.max())
print(amp.min())
print(freq.max())
print(freq.min())

plt.figure(figsize=(10, 5))
plt.plot(freq[:n//2], amp[:n//2])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')

# %%
