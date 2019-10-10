
import os
from scipy.io.wavfile import write
import numpy as np

fs = 16000
duration = 5
silent_audio = np.zeros(fs * duration, dtype=np.int16)
audio_path = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\silent_audio.wav"
write(audio_path, fs, silent_audio)