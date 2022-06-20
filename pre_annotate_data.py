#!/usr/bin/env python3
import warnings
import numpy as np
import os
import time
from subprocess import call
import cv2
import json
###############################################################################

Datadir = '/Volumes/COMPA/upward_facing_cameras_data/pre_processed_data/pre_processed_data_0629/frames_ufc_20_01_vi_0001_20190629_171132/'
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
###############################################################################

all_frames_dict = make_dict_per_frame(Datadir)

#create json file and dump the dictionary there
json_filename =  Outdir+'all_frames_dict.json'
print(json_filename)
with open(json_filename, "w") as write_file:
    json.dump(all_frames_dict, write_file, indent=4)
