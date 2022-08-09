# %%

import IPython.display as disp
import librosa
import librosa.display as libdisp

audio1, sr1 = librosa.load('./data/音声.mp3', sr=None, offset=0, duration=1)

audio1_sr22, sr1_sr22 = librosa.load(
    './data/音声.mp3', sr=22050, offset=0, duration=1)

audio1_sr8 = librosa.resample(audio1, sr1, 8000)

libdisp.waveshow(audio1, sr=sr1)
libdisp.waveshow(audio1_sr22, sr=sr1_sr22)
libdisp.waveshow(audio1_sr8, sr=8000)

audio2, sr2 = librosa.load('./data/携帯電話着信音.mp3', sr=None, offset=0, duration=1)

libdisp.waveshow(audio2, sr=sr2)


# %%
