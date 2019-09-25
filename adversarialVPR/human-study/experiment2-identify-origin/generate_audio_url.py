
import numpy as np
import os
import pandas as pa

root_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\experiment2-identify-origin"
pair_iter = os.listdir(root_dir)

origin_urls = []
adver_urls = []
prefix = "https://golferchen.github.io/adversarialVPR/human-study/experiment2-identify-origin/"

for pair_name in pair_iter:
    pair_dir = os.path.join(root_dir, pair_name)

    if os.path.isfile(pair_dir):
        continue

    audio_iter = os.listdir(pair_dir)
    for audio_name in audio_iter:

        url = prefix + pair_name + "/" + audio_name

        if audio_name.split("-")[0] == "origin":
            origin_urls.append(url)
        elif audio_name.split("-")[0] == "adver":
            adver_urls.append(url)

data = {"origin_url": origin_urls , "adver_url": adver_urls}

df = pa.DataFrame(data)
print(df),
df.to_csv("D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\experiment2-identify-origin\\audio_url.csv")
