
import numpy as np
import os
import random
from shutil import copyfile
import pandas as pa

root_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\experiment1-clean-noisy-multiple-epsilon"
des_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\experiment1-clean-noisy-multiple-epsilon"
audio_path_list = []
flag_list = []
architecture_list = []
task_list = []
epsilon_list = []

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

        if dir_name == "adversarial":
            architecture = audio_name.split("-")[0]
            task = audio_name.split("-")[1]
            epsilon = audio_name.split("-")[2]
        else:
            architecture = "None"
            task = "None"
            epsilon = "None"

        architecture_list.append(architecture)
        task_list.append(task)
        epsilon_list.append(epsilon)



#random.shuffle(audio_path_list)
n_audios = len(audio_path_list)
index = np.random.choice(n_audios, n_audios, replace=False, p=None)

src_audios = []
flags = []
des_audios = []
architectures = []
tasks = []
epsilons = []

for i, index_ in enumerate(index):

    src_audio_path = audio_path_list[index_]
    flag = flag_list[index_]
    des_audio_path = os.path.join(des_dir, str(i+1) + ".wav")
    copyfile(src_audio_path, des_audio_path)

    src_audios.append(src_audio_path)
    des_audios.append(des_audio_path)
    flags.append(flag)

    architecture = architecture_list[index_]
    task = task_list[index_]
    epsilon = epsilon_list[index_]
    architectures.append(architecture)
    tasks.append(task)
    epsilons.append(epsilon)

data = {"des": des_audios, "src": src_audios, "flag": flags, "architecture": architectures, "task": tasks, "epsilon": epsilons}
df = pa.DataFrame(data)
df.to_csv("D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\experiment1-clean-noisy-multiple-epsilon\\info.csv")






