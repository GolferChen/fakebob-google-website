
import numpy as np
import os
import pandas as pd

root_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\experiment3-identify-speaker"
spk_iter = os.listdir(root_dir)

prefix = "https://golferchen.github.io/adversarialVPR/human-study/experiment3-identify-speaker/"
ground_audio_urls = []
audio_urls = []

for spk_id in spk_iter:

    spk_dir = os.path.join(root_dir, spk_id)

    if os.path.isfile(spk_dir):
        continue

    audio_iter = os.listdir(spk_dir)
    n_audios = len(audio_iter) - 1
    for audio_name in audio_iter:

        url = prefix + spk_id + "/" + audio_name

        if audio_name.split("-")[0] == "ground":
            ground_audio_urls += [url for i in range(n_audios)]
        else:
            audio_urls.append(url)

data = {"ground_url": ground_audio_urls, "audio_url": audio_urls}
df = pd.DataFrame(data)
print(df),
df.to_csv("D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\experiment3-identify-speaker\\audio_url.csv")

