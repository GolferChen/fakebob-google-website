
import pandas as pd
import os

urls = []
prefix = "adversarialVPR/human-study/human-study-pre-test/amozon-mturk/experiment1-clean-noisy/"
audio_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\experiment1-clean-noisy"
audio_iter = os.listdir(audio_dir)
for audio_name in audio_iter:

    url = prefix + audio_name
    urls.append(url)

data = {"audio_url": urls}
df = pd.DataFrame(data)
df.to_csv("D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\exper1.csv")

"""
ground_urls = []
urls = []
prefix = "adversarialVPR/human-study/human-study-pre-test/amozon-mturk/experiment3-identify-speaker/"
root_dir = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\experiment3-identify-speaker"
spk_iter = os.listdir(root_dir)
for spk_id in spk_iter:
    spk_dir = os.path.join(root_dir, spk_id)

    if os.path.isfile(spk_dir):
        continue

    pair_iter = os.listdir(spk_dir)
    for pair_name in pair_iter:
        pair_dir = os.path.join(spk_dir, pair_name)
        audio_iter = os.listdir(pair_dir)
        for audio_name in audio_iter:
            url = prefix + "/" + spk_id + "/" + pair_name + "/" + audio_name
            if ("spk" in audio_name) or ("female" in audio_name):
                ground_urls.append(url)
            else:
                urls.append(url)

data = {"ground_url": ground_urls, "audio_url": urls}
df = pd.DataFrame(data)
df.to_csv("D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\exper3.csv")
"""


