#!/usr/bin/env python3
import warnings
import numpy as np
import os
import time
from subprocess import call
import cv2
import json
###############################################################################

Datadir = '/Volumes/COMPA/upward_facing_cameras_data/pre_processed_data/pre_processed_data_0629/frames_ufc_20_01_vi_0001_20190629_171133/'
Outdir = '/Volumes/COMPA/upward_facing_cameras_data/pre_processed_data/pre_processed_data_0629/'
###############################################################################

def make_dict_per_frame(Datadir):
    #Datadir directory named with the video name from which all frames where extracted
    #returns a list of dictionaries, each dictionary corresponds to a single frame
    frames = os.listdir(Datadir)
    values = ['filepath', 'id', 'videocode', 'experiment_date', 'camname', 'lenstype', 'datatype', 'labeled']

    all_frames_dict = []
    for i in range(len(frames)):
        frame_dict = {}
        frame_dict['filepath'] = Datadir+frames[i]
        frame_dict['id'] = i
        frame_dict['videocode'] = Datadir.split('/')[-2][7:]
        frame_dict['experiment_date'] = Datadir.split('/')[-3][-4:]
        frame_dict['camname'] = Datadir.split('/')[-2][7:11] + Datadir.split('/')[-2][14:16]
        frame_dict['lenstype'] = Datadir.split('/')[-2][11:13]

        if i <= int(len(frames)/2):
            frame_dict['datatype'] = 'pre_release'
        else:
            frame_dict['datatype'] = 'post_release'
        frame_dict['labeled'] = 0
        all_frames_dict.append(frame_dict)

    return all_frames_dict

def save_dict_to_json(my_list_of_dicts, my_json_filename):
    with open(my_json_filename, "w") as write_file:
        json.dump(my_list_of_dicts, write_file, indent=4)

def add_dicts_to_json(new_list_of_dicts, my_json_filename):
    f = open(my_json_filename)
    data_list = json.load(f)
    for i in range(len(new_list_of_dicts)):
        data_list.append(new_list_of_dicts[i])
    save_dict_to_json(data_list, my_json_filename)
    f.close()
###############################################################################

all_frames_dict = make_dict_per_frame(Datadir)

#create json file and dump the dictionary there
json_filename =  Outdir+'all_frames_dict.json'

save_new = 1
if save_new == 1:
    save_dict_to_json(all_frames_dict, json_filename)
else:
    pass
    #add_dicts_to_json(all_frames_dict, json_filename)

print('list of dictionaries saved', json_filename)
