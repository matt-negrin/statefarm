#!/Users/matthew.negrin/anaconda2/envs/fastai_py27/bin/python

import json

def kaggle_creds(json_file):
    with open(json_file) as data_file:    
        data = json.load(data_file)
    return data