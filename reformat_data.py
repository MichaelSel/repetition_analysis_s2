import os
import re
import json

def run():
    data_dir = './data'
    processed_dir = './processed'
    subjects = [{'id': x, 'dir': data_dir + "/" + x + "/csv"} for x in os.listdir(data_dir) if x.startswith("SVG")]
    for subject in subjects:
        files = [f for f in os.listdir(subject['dir']) if os.path.isfile(os.path.join(subject['dir'], f)) and f.startswith("SVG")]

        if(len(files)==0): continue; #If the subject folder is empty, move to the next subject

        if(len([f for f in files if "json" in f])==0):continue; #if subject did not complete any blocks, move to the next subject.


        subject["blocks"] = [{
            "dir": subject['dir'] + "/" + f,
            "block": int(re.findall(r'\d+', f)[-1])
        } for f in files if "json" in f] #put all the blocks in subject["blocks"]


        subject["blocks"] = sorted(subject["blocks"], key=lambda i: i['block']) #makes sure the blocks are sorted numerically and not alphabetically
        blocks = [];
        for item in subject['blocks']: blocks.insert(item['block'], item);
        subject['blocks'] = blocks

        for results_json in subject["blocks"]:
            json_file = open(results_json['dir'])
            json_file = json_file.read()

            block = json.loads(json_file)
            repetition = [entry for entry in block if entry['name'] == 'choice']
            results_json['repetition'] = repetition
    json_export = json.dumps(subjects)
    f = open(processed_dir + "/repetition_all_subjects.json", "w")
    f.write(json_export)
    f.close()
    print("Reformatted data.")

