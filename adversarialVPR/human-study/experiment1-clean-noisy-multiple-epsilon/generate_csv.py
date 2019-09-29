
import numpy as np
import os
import random
import pandas as pd

prefix = "https://golferchen.github.io/adversarialVPR/human-study/experiment1-clean-noisy/"
col_name = "audio_url"

root_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\experiment1-clean-noisy"
dir_iter = os.listdir(root_dir)

url_list = []

for dir_name in dir_iter:
    child_dir = os.path.join(root_dir, dir_name)

    if not os.path.isdir(child_dir):
        continue

    audio_iter = os.listdir(child_dir)

    for audio_name in audio_iter:

        if audio_name.split(".")[-1] == "flac":
            continue

        url = prefix + dir_name + "/" + audio_name

        print(url),

        url_list.append(url)

random.shuffle(url_list)
data = {col_name:url_list}
df = pd.DataFrame(data)
print(df),
df.to_csv("D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\experiment1-clean-noisy\\audio_url.csv")

