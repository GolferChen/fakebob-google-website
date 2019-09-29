
import numpy as np
import os
import random
from shutil import copyfile
import pandas as pa

root_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\experiment1-clean-noisy"
des_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\experiment1-clean-noisy"
audio_path_list = []
flag_list = []
dir_iter = os.listdir(root_dir)
for dir_name in dir_iter:

    child_dir = os.path.join(root_dir, dir_name)

    if os.path.isfile(child_dir):
        continue

    audio_iter = os.listdir(child_dir)

    flag = dir_name

    for audio_name in audio_iter:
        audio_path = os.path.join(child_dir, audio_name)
        audio_path_list.append(audio_path)
        flag_list.append(flag)

#random.shuffle(audio_path_list)
n_audios = len(audio_path_list)
index = np.random.choice(n_audios, n_audios, replace=False, p=None)

src_audios = []
flags = []
des_audios = []

for i, index_ in enumerate(index):

    src_audio_path = audio_path_list[index_]
    flag = flag_list[index_]
    des_audio_path = os.path.join(des_dir, str(i+1) + ".wav")
    copyfile(src_audio_path, des_audio_path)

    src_audios.append(src_audio_path)
    des_audios.append(des_audio_path)
    flags.append(flag)

data = {"des": des_audios, "src": src_audios, "flag": flags}
df = pa.DataFrame(data)
df.to_csv("D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\experiment1-clean-noisy\\info.csv")






