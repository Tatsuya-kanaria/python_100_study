# %%

import librosa

audio1, sr1 = librosa.load('./data/音声.mp3', sr=None)
print(audio1)
print(sr1)

print(audio1.shape)
print(audio1.max())
print(audio1.min())

audio2, sr2 = librosa.load('./data/携帯電話着信音.mp3', sr=None)
print(audio2)
print(sr2)

print(audio2.shape)

# %%
