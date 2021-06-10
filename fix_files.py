import os
import re
import json

data_dir = './data'
subjects = [{'id': x, 'dir': data_dir + "/" + x + "/csv"} for x in os.listdir(data_dir) if x.startswith("SVG")]
for subject in subjects:
    resp_files = [f for f in os.listdir(subject['dir']) if os.path.isfile(os.path.join(subject['dir'], f)) and f.startswith("SVG")]
    task_files = [f for f in os.listdir(subject['dir']) if os.path.isfile(os.path.join(subject['dir'], f)) and f.startswith("block") and f.endswith('.json')]
    for i in range(4):
        resp_file_path = subject['dir'] + '/' + resp_files[i]
        task_file_path = subject['dir'] + '/' + task_files[i]
        resp_file = open(resp_file_path)
        resp_file = resp_file.read()
        resp = json.loads(resp_file)

        task_file = open(task_file_path)
        task_file = task_file.read()
        task = json.loads(task_file)

        for j in range(len(resp)):
            resp[j]['order'] = task[j]['order']
            print(resp[j]['order'])

        json_export = json.dumps(resp)
        f = open(resp_file_path, "w")
        f.write(json_export)
        f.close()