import json
import csv
import scipy.stats
import numpy as np
import reformat_data
import statistics as stat



#define directories
processed_dir = './processed'
analyzed_dir = './analyzed'
all_data_path = processed_dir + "/repetition_all_subjects.json"
responses_excluded=0

all_sets = []


def get_json(path):
        json_file = open(path)
        json_file = json_file.read()
        return json.loads(json_file)

def mean(ls):
        if len(ls)>0:
                return stat.mean(ls)
        return float('NaN')

def make_csv(subs, keys_to_store,filename='/repetition_results_new.csv'):
        subs = [sub for sub in subs if 'analyzed' in sub] #only analyze subjects that have data
        with open(analyzed_dir + filename, 'w', newline='') as file:
                writer = csv.writer(file)
                keys = ['Subject_ID','excluded','pressed_button1','pressed_button2']
                for i in range(len(all_sets)):
                        set_name = 'set_' + str(i+1)
                        keys.append(set_name)
                        for key in keys_to_store:
                                keys.append(set_name + "_" + key)
                writer.writerow(keys)

                for s in subs:
                        values = [s['id'],s['excluded'],s['analyzed']['pressed_button1'],s['analyzed']['pressed_button2']]
                        for i in range(len(all_sets)):
                                set_key = all_sets[i]
                                values.append(set_key)
                                if(set_key not in s['analyzed']['sets']):
                                        for key in keys_to_store:
                                                values.append(" ")
                                else:
                                        for key in keys_to_store:
                                                if(key not in s['analyzed']['sets'][set_key]): values.append("ERROR")
                                                values.append(s['analyzed']['sets'][set_key][key])
                        writer.writerow(values)
        print("Aggregate analysis file saved.")
        return False

def make_json(subs):
        json_export = json.dumps(subs)
        f = open(analyzed_dir + "/repetition_results_new.json", "w")
        f.write(json_export)
        f.close()
        print("saved data.")

reformat_data.run()

all_subjects = get_json(all_data_path)
for s in all_subjects: #every subject in the cohort
        s['excluded']=False
        s['analyzed']={
                'block':[],
                'sets':{}
        }
        block_ids_to_run = [block['block'] for block in s['blocks']]

        #you can run specific blocks by uncommenting below
        # block_ids_to_run = [1]

        #This task doesn't have a practice block
        # #don't run the practice block:
        # block_ids_to_run.remove(0) #practice block is index 0

        for block in s['blocks']: #every block for the subject
                if(block['block'] not in block_ids_to_run): continue #if it's not in the blocks we want, skip it
                data = {
                        'sets':{},
                        # 'trials_total': 0,
                        # 'chose_diatonic': 0,
                        # 'chose_chromatic': 0,
                        # 'rts':[],
                        # 'rt_diatonic':[],
                        # 'rt_chromatic': [],
                        'pressed_button1':0,
                        'pressed_button2': 0,
                }
                for Q in block['repetition']: #Q is every question/trial in the block
                        Q['excluded'] = False
                        # Trial level Time-based exclusion should be written here

                        if(Q['name']!='choice'): continue #if not a choice question, continue to next Q

                        if(Q['response']=='1st'):
                                response_pos = 0
                                data['pressed_button1']+=1
                        elif (Q['response'] == '2nd'):
                                response_pos = 1
                                data['pressed_button2'] += 1
                        else:
                                print("there was an error.")
                        necklace = ', '.join([str(digit) for digit in Q['necklace']])
                        if(necklace not in all_sets):all_sets.append(necklace) #Track all analyzed sets for all subjects in global variable
                        if(necklace not in data['sets']):
                                data['sets'][necklace] = {
                                        'trials_total': 0,
                                        'chose_diatonic': 0,
                                        'chose_chromatic': 0,
                                        'rts':[],
                                        'rt_diatonic':[],
                                        'rt_chromatic': [],
                                }
                        # increment trial tally
                        cur_set = data['sets'][necklace]
                        cur_set['trials_total'] +=1
                        cur_set['rts'].append(Q['rt'])
                        if(Q['order'][response_pos]=='diatonic'):
                                cur_set['chose_diatonic'] += 1
                                cur_set['rt_diatonic'].append(Q['rt'])
                        elif (Q['order'][response_pos] == 'chromatic'):
                                cur_set['chose_chromatic'] += 1
                                cur_set['rt_chromatic'].append(Q['rt'])


                s['analyzed']['block'].append(data)

                #once all the per block data was collected(above), append it to subject totales:
                #if the key doesn't exist in the subject level, create it, otherwise, add to it
                for key in data:
                        if (key =="sets"): continue  # don't do it for sets. Sets are handled below
                        try:
                                s['analyzed'][key] += data[key]
                        except:
                                s['analyzed'][key] = data[key]


                '''Here we handle sets'''
                for st in data['sets']:
                        if(st not in s['analyzed']['sets']): s['analyzed']['sets'][st]={}
                        for key in data['sets'][st]:
                                try:
                                        s['analyzed']['sets'][st][key] += data['sets'][st][key]
                                except:
                                        s['analyzed']['sets'][st][key] = data['sets'][st][key]



        for set in s['analyzed']['sets']:
                necklace = s['analyzed']['sets'][set]
                if(necklace['trials_total']!=0):
                        necklace['%_diatonic'] = necklace['chose_diatonic'] / necklace['trials_total']
                        necklace['%_chromatic'] = necklace['chose_chromatic'] / necklace['trials_total']
                        necklace['rt_diatonic'] = mean(necklace['rt_diatonic'])
                        necklace['rt_chromatic'] = mean(necklace['rt_chromatic'])
                        necklace['rt'] = mean(necklace['rts'])
                        necklace['rt_diatonic:average'] = necklace['rt_diatonic'] / necklace['rt']
                        necklace['rt_chromatic:average'] = necklace['rt_chromatic'] / necklace['rt']


keys_to_store = ['trials_total','chose_diatonic', 'chose_chromatic','%_diatonic','%_chromatic','rt_diatonic','rt_chromatic','rt','rt_diatonic:average','rt_chromatic:average']





make_csv(all_subjects, keys_to_store)

make_json(all_subjects)



