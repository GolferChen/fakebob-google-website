
import pandas as pd
import os
import copy

clean = "Clean"
noisy = "Noisy"
not_sure = "Not"

reject_comment = "You fail our concentration test. We conclude that you choose the option randomly"
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

data_new = copy.deepcopy(data)
workers = data_new.ix[:, "WorkerId"]
approve = data_new.ix[:, "Approve"]
reject = data_new.ix[:, "Reject"]

reject_cnt = 0
approve_cnt = 0

for i, worker in enumerate(workers):

    if worker in exclusive_workers:

        reject[i] = reject_comment

        reject_cnt += 1

    else:

        approve[i] = "x"

        approve_cnt += 1

#data_new.to_csv("D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\MTurk_exper1_reject_result.csv")
print(approve_cnt, reject_cnt)




