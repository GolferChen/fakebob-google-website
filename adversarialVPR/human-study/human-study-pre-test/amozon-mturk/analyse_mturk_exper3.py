
import os
import pandas as pd

origin_id = [2, 7, 8, 13, 16, 17, 29, 30, 36]
other_id = [6, 9, 11, 15, 18, 21, 25, 27, 35]
adver_id = [3, 4, 5, 10, 19, 24, 28, 31, 33]
adver_small_id = [3, 5, 10, 19, 24, 28]
adver_big_id = [4, 31, 33]

origin = "origin"
other = "other"
adver = "adver"
adver_small = "adver_samll"
adver_big = "adver_big"

same = "Same"
different = "Different"
not_sure = "Not"

def get_type(number):

    if number in origin_id:
        return origin

    if number in other_id:
        return other

    if number in adver_id:
        return adver

def get_adver_type(number):

    if not number in adver_id:
        print("wrong!!!!!!!!!!!")
        return None

    if number in adver_small_id:
        return adver_small

    if number in adver_big_id:
        return adver_big

results = {origin: {same: 0, different: 0, not_sure: 0},
           other: {same: 0, different: 0, not_sure: 0},
           adver: {same: 0, different: 0, not_sure: 0},
           adver_small: {same: 0, different: 0, not_sure: 0},
           adver_big: {same: 0, different: 0, not_sure: 0}}

csv_path = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\Batch_3795612_batch_results.csv"
data = pd.read_csv(csv_path)
urls = data.ix[:, "Input.audio_url"]
answers = data.ix[:, "Answer.experiment3-identify-speaker.label"]
workers = data.ix[:, "WorkerId"]
used_times = data.ix[:, "WorkTimeInSeconds"]

exclusive_workers = ["AJ1Q54P37KT5R", "A3P9TMATWBA1QP", "A5DYCKQZA0XYQ", "A2L746JBCNW066", "A12RIQW8ULF0VX",
                     "A17LA7KM9S0SCS", "A387XZP0I4XXAF", "A3P9TMATWBA1QP", "ATMD452KBHND8", "A3S6PT01MUIVYY", "A10AY39RH8ZB7I",
                     "A17LA7KM9S0SCS", "A17VT1UHC6R911", "ATMD452KBHND8"]

n_workers = len(set(workers))
n_workers_exclusive = len(set(exclusive_workers))
print("%d, %d, %d"%(n_workers, n_workers_exclusive, n_workers - n_workers_exclusive)),

'''
exclusive_workers = []
statistic_workers = {}
for worker in workers:
    if worker in statistic_workers:
        statistic_workers[worker] += 1
    else:
        statistic_workers[worker] = 1

num = 30
keys = statistic_workers.keys()
for key in keys:
    if statistic_workers[key] != num:
        exclusive_workers.append(key)

exclusive_workers += ["AJ1Q54P37KT5R", "A3P9TMATWBA1QP", "A5DYCKQZA0XYQ", "A2L746JBCNW066", "A12RIQW8ULF0VX",
                     "A17LA7KM9S0SCS", "A387XZP0I4XXAF", "A3P9TMATWBA1QP", "ATMD452KBHND8", "A3S6PT01MUIVYY", "A10AY39RH8ZB7I",
                     "A17LA7KM9S0SCS", "A17VT1UHC6R911", "ATMD452KBHND8"]
'''

verification_workers = []
for worker, url in zip(workers, urls):

    if not ("male" in url):
        continue

    if worker in verification_workers:
        continue

    if (not (worker in verification_workers)) and (not (worker in exclusive_workers)):
        verification_workers.append(worker)

print(len(verification_workers)),

for worker_id, url, answer, used_time in zip(workers, urls, answers, used_times):

    #if worker_id in exclusive_workers:
        #continue

    if "male" in url:
        continue

    if not (worker_id in verification_workers):
        print("continue")
        continue

    #if used_time < 30:
        #continue

    number = int(url.split("/")[-1].split(".")[0])
    flag = get_type(number)
    answer_part = answer.split(" ")[0]
    results[flag][answer_part] += 1

    #print(number, flag, answer_part),

    if flag == adver:
        adver_flag = get_adver_type(number)
        results[adver_flag][answer_part] += 1

#for flag in [origin, other, adver]:
for flag in [origin, other, adver, adver_small, adver_big]:

    same_cnt = results[flag][same]
    different_cnt = results[flag][different]
    not_sure_cnt = results[flag][not_sure]
    total_cnt = same_cnt + different_cnt + not_sure_cnt

    same_rate = same_cnt * 100 / total_cnt
    different_rate = different_cnt * 100 / total_cnt
    not_sure_rate = not_sure_cnt * 100 / total_cnt

    print("%s, %d, %d, %f, %d, %f, %d, %f"%(flag, total_cnt, same_cnt, same_rate, different_cnt, different_rate, not_sure_cnt, not_sure_rate)),





