import csv
import pandas as pd
def csv_to_pandas(file_path,format):
    def get_csv(path):
        with open(path) as f:
            a = [{k: v for k, v in row.items()}
                 for row in csv.DictReader(f, skipinitialspace=True)]
        return a

    subjects = get_csv(file_path)

    data = []
    for subject in subjects:
        for category in format:
            structure = {}
            for el in category['static']:
                structure[el] = category['static'][el]
            for el in category['dynamic']:
                structure[el] = subject[category['dynamic'][el]]
            data.append(structure)
    return pd.DataFrame(data)





