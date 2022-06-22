#!/usr/bin/env python3
import warnings
import numpy as np
import os
import time
from subprocess import call
import cv2
import json
###############################################################################

DataDirs = ['/Volumes/My Passport/upward_facing_cameras_data/work_ufcs/work_0419_videos_2/trimmed_videos/',
            '/Volumes/My Passport/upward_facing_cameras_data/work_ufcs/work_0508_videos/trimmed_videos/',
            '/Volumes/My Passport/upward_facing_cameras_data/work_ufcs/work_0611_videos/trimmed_videos/',
            '/Volumes/My Passport/upward_facing_cameras_data/work_ufcs/work_0629_videos/trimmed_videos/',
            '/Volumes/My Passport/upward_facing_cameras_data/work_ufcs/work_0706_videos/trimmed_videos/',
            '/Volumes/My Passport/upward_facing_cameras_data/work_ufcs/work_0718_videos/trimmed_videos/']

Outdir = '/Users/fponce/Documents/cv4e/'

all_experiment_dates = ['0419', '0508', '0611', '0629', '0706', '0718']
###############################################################################

def make_dict_per_video(videopaths):
    #list of paths to videos
    #returns a list of dictionaries, each dictionary corresponds to metadata of single video

    values = ['videopath', 'videocode', 'experiment_date']

    all_videos_dict = []
    for i in range(len(videopaths)):
        video_dict = {}
        video_dict['videopath'] = videopaths[i]
        video_dict['videocode'] = videopaths[i].split('/')[-1][0:-4]
        filename = videopaths[i].split('/')[-1]
        date_location = (filename.find('2019', 1))
        video_dict['experiment_date'] = filename[date_location+4:date_location+8]

        all_videos_dict.append(video_dict)

    return all_videos_dict

def save_dict_to_json(my_list_of_dicts, my_json_filename):
    with open(my_json_filename, "w") as write_file:
        json.dump(my_list_of_dicts, write_file, indent=4)
###############################################################################


all_videos_paths = []
for d in range(len(DataDirs)):
    print(DataDirs[d])
    for dirpath, dirnames, filenames in os.walk(DataDirs[d]):
        for filename in [f for f in filenames if f.endswith(".mp4")]:
            file_name = os.path.join(dirpath, filename)
            basename = os.path.basename(file_name)
            print(basename)
            all_videos_paths.append(file_name)

all_videos_dict = make_dict_per_video(all_videos_paths)
print(len(all_videos_dict))

#create json file and dump the dictionary there
json_filename =  Outdir+'all_videos_dict.json'

save_new = 1
if save_new == 1:
    save_dict_to_json(all_videos_dict, json_filename)
else:
    pass

print('list of dictionaries saved', json_filename)
