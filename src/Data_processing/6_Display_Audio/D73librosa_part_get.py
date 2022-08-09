# %%

import IPython.display as disp
import librosa

audio2, sr2 = librosa.load('./data/携帯電話着信音.mp3', sr=None, offset=0, duration=1)
print(audio2)
print(sr2)

print(audio2.shape)

disp.Audio(data=audio2, rate=sr2)

# %%
