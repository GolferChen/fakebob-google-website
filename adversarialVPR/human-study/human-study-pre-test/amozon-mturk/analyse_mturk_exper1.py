
import pandas as pd
import os

clean = "Clean"
noisy = "Noisy"
not_sure = "Not"

origin = "origin"
adver = "adver"
adver_small = "adver_small"
adver_big = "adver_big"

origin_id = [1, 3, 7, 19, 21, 22, 23, 25, 26, 27, 34, 36]
adver_id = [2, 5, 6, 8, 10, 12, 16, 17, 18, 20, 24, 30, 31, 33, 35]
adver_small_id = [2, 5, 6, 8, 10, 17, 20, 24, 30, 31, 33, 35]
adver_big_id = [12, 16, 18]

def get_flag(number):

    if number in origin_id:
        return origin

    if number in adver_id:
        return adver

def get_adver_flag(number):

    if not (number in adver_id):
        print("Wrong")
        return None

    if number in adver_small_id:
        return adver_small

    if number in adver_big_id:
        return adver_big

csv_path = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\Batch_3796944_batch_results.csv"
data = pd.read_csv(csv_path)
workers = data.ix[:, "WorkerId"]
answers = data.ix[:, "Answer.experiment1-clean-noisy.label"]
urls = data.ix[:, "Input.audio_url"]

exclusive_workers = set()

for worker, url, answer in zip(workers, urls, answers):

    if not ("silent" in url):
        continue

    answer_part = answer.split(" ")[0]

    if answer_part == noisy:
        exclusive_workers.add(worker)

print(exclusive_workers),
n_workers_total = len(set(workers))
n_workers_exclusive = len(exclusive_workers)
print("%d, %d, %d"%(n_workers_total, n_workers_exclusive, n_workers_total - n_workers_exclusive)),

results = {origin: {clean: 0, noisy: 0, not_sure: 0},
           adver: {clean: 0, noisy: 0, not_sure: 0},
           adver_small: {clean: 0, noisy: 0, not_sure: 0},
           adver_big: {clean: 0, noisy: 0, not_sure: 0}}

contain_cp_workers = set()
for worker, url, answer in zip(workers, urls, answers):

    if not ("silent" in url):
        continue

    if not (worker in exclusive_workers):
        contain_cp_workers.add(worker)

print(len(contain_cp_workers)),

for worker, url, answer in zip(workers, urls, answers):

    if "silent" in url:
        continue

    if worker in exclusive_workers:
        continue

    #if not (worker in contain_cp_workers):
        #continue

    number = int(url.split("/")[-1].split(".")[0])
    flag = get_flag(number)
    answer_part = answer.split(" ")[0]
    results[flag][answer_part] += 1

    if flag == adver:

        adver_flag = get_adver_flag(number)
        results[adver_flag][answer_part] += 1

for flag in [origin, adver, adver_small, adver_big]:

    clean_cnt = results[flag][clean]
    noisy_cnt = results[flag][noisy]
    not_sure_cnt = results[flag][not_sure]
    total_cnt = clean_cnt + noisy_cnt + not_sure_cnt

    clean_rate = clean_cnt * 100 / total_cnt
    noisy_rate = noisy_cnt * 100 / total_cnt
    not_sure_rate = not_sure_cnt * 100 / total_cnt

    print("%s, %d, %d, %f, %d, %f, %d, %f"%(flag, total_cnt, clean_cnt, clean_rate, noisy_cnt, noisy_rate, not_sure_cnt, not_sure_rate)),






