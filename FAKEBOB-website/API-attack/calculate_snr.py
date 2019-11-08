
import os
from scipy.io.wavfile import read
import numpy as np
import pickle

# audio_dir = "D:/Git/GolferChen.github.io/FAKEBOB-website/API-attack/OSI"
# audio_iter = os.listdir(audio_dir)
#
# intra_original_audio_name = "intra-original-male-260-123288-0013.wav"
# intra_original_audio_path = audio_dir + "/" + intra_original_audio_name
# _, intra_original_audio = read(intra_original_audio_path)
# intra_original_audio = intra_original_audio / (2 ** (16 - 1))
# intra_original_power = np.sum(np.power(intra_original_audio, 2))
#
# inter_original_audio_name = "inter-original-male-6930-81414-0009.wav"
# inter_original_audio_path = audio_dir + "/" + inter_original_audio_name
# _, inter_original_audio = read(inter_original_audio_path)
# inter_original_audio = inter_original_audio / (2 ** (16 - 1))
# inter_original_power = np.sum(np.power(inter_original_audio, 2))
#
# for audio_name in audio_iter:
#
#     if audio_name == intra_original_audio_name or audio_name == inter_original_audio_name:
#         continue
#
#     audio_path = audio_dir + "/" + audio_name
#
#     if audio_name.split("-")[0] == "intra":
#         baseline_power = intra_original_power
#         original_audio = intra_original_audio
#     else:
#         baseline_power = inter_original_power
#         original_audio = inter_original_audio
#
#     _, adver_audio = read(audio_path)
#     adver_audio = adver_audio / (2 ** (16 - 1))
#     noise = adver_audio - original_audio
#     noise_power = np.sum(np.power(noise, 2))
#     snr = 10 * np.log10(baseline_power / noise_power)
#
#     print("%s, %.2f" %(audio_name.split("-")[1], snr)),


# audio_dir = "D:/Git/GolferChen.github.io/FAKEBOB-website/API-attack/SV"
# audio_iter = os.listdir(audio_dir)
#
# intra_original_audio_name = "intra-original-6930-81414-0010.wav"
# intra_original_audio_path = audio_dir + "/" + intra_original_audio_name
# _, intra_original_audio = read(intra_original_audio_path)
# intra_original_audio = intra_original_audio / (2 ** (16 - 1))
# intra_original_power = np.sum(np.power(intra_original_audio, 2))
#
# inter_original_audio_name = "inter-original-237-134493-0016.wav"
# inter_original_audio_path = audio_dir + "/" + inter_original_audio_name
# _, inter_original_audio = read(inter_original_audio_path)
# inter_original_audio = inter_original_audio / (2 ** (16 - 1))
# inter_original_power = np.sum(np.power(inter_original_audio, 2))
#
# for audio_name in audio_iter:
#
#     if audio_name == intra_original_audio_name or audio_name == inter_original_audio_name:
#         continue
#
#     audio_path = audio_dir + "/" + audio_name
#
#     if audio_name.split("-")[0] == "intra":
#         baseline_power = intra_original_power
#         original_audio = intra_original_audio
#     else:
#         baseline_power = inter_original_power
#         original_audio = inter_original_audio
#
#     _, adver_audio = read(audio_path)
#     adver_audio = adver_audio / (2 ** (16 - 1))
#     noise = adver_audio - original_audio
#     noise_power = np.sum(np.power(noise, 2))
#     snr = 10 * np.log10(baseline_power / noise_power)
#
#     print("%s, %.2f" %(audio_name.split("-")[0], snr)),

# audio_dir = "D:/Git/GolferChen.github.io/FAKEBOB-website/API-attack/CSI"
# audio_iter = os.listdir(audio_dir)
#
# intra_original_audio_name = "intra-original-female-4446-2273-0027.wav"
# intra_original_audio_path = audio_dir + "/" + intra_original_audio_name
# _, intra_original_audio = read(intra_original_audio_path)
# intra_original_audio = intra_original_audio / (2 ** (16 - 1))
# intra_original_power = np.sum(np.power(intra_original_audio, 2))
#
# inter_original_audio_name = "inter-original-female-5142-33396-0056.wav"
# inter_original_audio_path = audio_dir + "/" + inter_original_audio_name
# _, inter_original_audio = read(inter_original_audio_path)
# inter_original_audio = inter_original_audio / (2 ** (16 - 1))
# inter_original_power = np.sum(np.power(inter_original_audio, 2))
#
# for audio_name in audio_iter:
#
#     if audio_name == intra_original_audio_name or audio_name == inter_original_audio_name:
#         continue
#
#     audio_path = audio_dir + "/" + audio_name
#
#     if audio_name.split("-")[0] == "intra":
#         baseline_power = intra_original_power
#         original_audio = intra_original_audio
#     else:
#         baseline_power = inter_original_power
#         original_audio = inter_original_audio
#
#     _, adver_audio = read(audio_path)
#     adver_audio = adver_audio / (2 ** (16 - 1))
#     noise = adver_audio - original_audio
#     noise_power = np.sum(np.power(noise, 2))
#     snr = 10 * np.log10(baseline_power / noise_power)
#
#     print("%s, %s, %.2f" %(audio_name.split("-")[0], audio_name.split("-")[3], snr)),

cp_dir = "D:/Git/GolferChen.github.io/FAKEBOB-website/API-attack/CSI-CP"
cp_iter = os.listdir(cp_dir)

for cp_name in cp_iter:

    cp_path = cp_dir + "/" + cp_name

    with open(cp_path, "rb") as reader:
        cp = pickle.load(reader)
        n_iter = len(cp)

    print("%s, %s, %d" %(cp_name.split("-")[0], cp_name.split("-")[3], n_iter)),

