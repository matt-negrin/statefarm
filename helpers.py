#!/Users/matthew.negrin/anaconda2/envs/fastai_py27/bin/python

import os
import json

def kaggle_creds(json_file):
    with open(json_file) as data_file:    
        data = json.load(data_file)
    return data

def kaggle_download(creds, competition):
    username = creds['kaggle_username']
    password = creds['kaggle_password']
    command = 'kg download -u ' + username + ' -p ' + password + ' -c ' + competition
    os.system(command)