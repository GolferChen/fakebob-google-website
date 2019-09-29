
import numpy as np
import os
import random
from shutil import copyfile
import pandas as pa
import xlsxwriter

root_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\experiment3-identify-speaker"
workbook = xlsxwriter.Workbook("D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\experiment3-identify-speaker\\info.xlsx")

dir_iter = os.listdir(root_dir)

audio_cnt = 1
pair_cnt = 1

for dir_name in dir_iter:
    spk_dir = os.path.join(root_dir, dir_name)

    if os.path.isfile(spk_dir):
        continue

    audio_path_list = []
    flag_list = []
    architecture_list = []
    task_list = []
    epsilon_list = []
    ground_audio_path = ""

    worksheet = workbook.add_worksheet(dir_name)
    row = 0
    col = 0

    audio_iter = os.listdir(spk_dir)
    for audio_name in audio_iter:
        audio_path = os.path.join(spk_dir, audio_name)

        if audio_name.split("-")[0] == "ground":
            ground_audio_path = audio_path
        else:
            audio_path_list.append(audio_path)
            flag = audio_name.split("-")[0]
            if flag == "adver":
                architecture = audio_name.split("-")[1]
                task = audio_name.split("-")[2]
                epsilon = audio_name.split("-")[3]
            else:
                architecture = "None"
                task = "None"
                epsilon = "None"

            flag_list.append(flag)
            architecture_list.append(architecture)
            task_list.append(task)
            epsilon_list.append(epsilon)

    n_audios = len(audio_path_list)
    index = np.random.choice(n_audios, n_audios, replace=False, p=None)
    pairs = []
    audios = []
    flags = []
    architectures = []
    tasks = []
    epsilons = []

    for i, index_ in enumerate(index):

        #des_dir = os.path.join(spk_dir, "pair-" + str(i+1))
        des_dir = os.path.join(spk_dir, "pair-" + str(pair_cnt))
        if not os.path.exists(des_dir):
            os.makedirs(des_dir)

        copyfile(ground_audio_path, os.path.join(des_dir, dir_name + ".wav"))
        copyfile(audio_path_list[index_], os.path.join(des_dir, str(audio_cnt) + ".wav"))
        audio_cnt += 1

        pairs.append("pair-" + str(pair_cnt))
        audios.append(audio_path_list[index_])
        flags.append(flag_list[index_])
        architectures.append(architecture_list[index_])
        tasks.append(task_list[index_])
        epsilons.append(epsilon_list[index_])

        pair_cnt += 1

    pairs = ["pair"] + pairs
    audios = ["audio"] + audios
    flags = ["flag"] + flags
    architectures = ["architecture"] + architectures
    tasks = ["task"] + tasks
    epsilons = ["epsilon"] + epsilons

    for pair, audio_path, flag, architecture, task, epsilon in zip(pairs, audios, flags, architectures, tasks, epsilons):

        worksheet.write(row, col, pair)
        worksheet.write(row, col + 1, audio_path)
        worksheet.write(row, col + 2, flag)
        worksheet.write(row, col + 3, architecture)
        worksheet.write(row, col + 4, task)
        worksheet.write(row, col + 5, epsilon)

        row += 1

workbook.close()





