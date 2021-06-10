import json
import dateutil.parser
import math
import statistics as stat
import csv
import scipy.stats
import os
import numpy as np
import sim_reformat_data
import matplotlib.pyplot as plt
import statistics as stat

#define directories
processed_dir = './processed'
analyzed_dir = './analyzed'
all_data_path = processed_dir + "/similarity_all_subjects.json"



def get_json(path):
        json_file = open(path)
        json_file = json_file.read()
        return json.loads(json_file)



all_subjects = get_json(all_data_path)
times = []

for s in all_subjects:
        if("DNOVS16" not in s['id']): continue

        start = s['blocks'][1]['similarity'][0]['time']
        finish = s['blocks'][-1]['similarity'][-1]['time']
        start = dateutil.parser.isoparse(start)
        finish = dateutil.parser.isoparse(finish)
        diff = finish-start
        diff = round(diff.total_seconds()/60)
        times.append(diff)
        print(s['id'],'took',diff,'minutes')

plt.hist(times, density=True, bins=200)  # `density=False` would make counts
plt.xlim([0, 100])
plt.show()


print('\n\n')
print("Average time for entire study",stat.mean(times),'minutes.')
print("Median time for entire study",stat.median(times),'minutes.')
print("Fastest time for entire study",min(times),'minutes.')
print("Slowest time for entire study",max(times),'minutes.')
print('\n')

print("Average time per question",stat.mean(times)*60/100,'seconds.')
print("Median time per question",stat.median(times)*60/100,'seconds.')
print("Fastest time per question",min(times)*60/100,'seconds.')
print("Slowest time per question",max(times)*60/100,'seconds.')

