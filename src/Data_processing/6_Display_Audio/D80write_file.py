# %%

import librosa
import librosa.display as libdisp
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as disp
import soundfile as sf

audio1, sr1 = librosa.load('./data/音声.mp3', sr=None, offset=0, duration=1)

audio1_sr22, sr1_sr22 = librosa.load(
    './data/音声.mp3', sr=22050, offset=0, duration=1)

audio1_sr8 = librosa.resample(audio1, sr1, 8000)

audio2, sr2 = librosa.load('./data/携帯電話着信音.mp3', sr=None)

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

# 時間を区切ってフーリエ変換する
# stft : Short-time Fourier transform


def colorbar_spectrogram(audio, sr):
    stft = librosa.stft(audio)
    amps = np.abs(stft)
    spectrogram = librosa.amplitude_to_db(amps)

    plt.figure(figsize=(10, 5))
    libdisp.specshow(spectrogram,
                     sr=sr,
                     x_axis='time',
                     y_axis='hz',
                     cmap='magma')

    bar = plt.colorbar()
    bar.ax.set_ylabel('db')


# colorbar_spectrogram(audio2, sr2)

# 高い音への変換
audio1_pitch = librosa.effects.pitch_shift(audio1, sr1, 10)

# 低い音への変換
audio1_pitch = librosa.effects.pitch_shift(audio1, sr1, -5)

# 時間の間延び
audio2_time = librosa.effects.time_stretch(audio2, 0.5)

audio2_time = librosa.effects.time_stretch(audio2, 2)

# データの書き出し
sr = 44100
sf.write('./data/audio2_time.wav', audio2_time, sr)


# %%
