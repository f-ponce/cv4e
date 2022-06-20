#!/usr/bin/env python3
from __future__ import print_function
import numpy
from subprocess import call
import os.path
import datetime
import sys
import skytracker
import time
from skytracker import SkyTracker

#convert videos from h264 to mp4 if necessary using "convert_UFCV_h264_2_mp4.py"

# input raw video directorypip install numpy
DataDir = '/home/fponce/field_data_0629'
t = time.strftime("%Y%m%d_%H%M%S", time.localtime())
experiment_date="0629"

# release time to cut videos before running blob finder
release_t = "17_43_20"
release_t_in_secs = (int(release_t[0:2])*3600+(int(release_t[3:5])*60)+(int(release_t[6:8])))
print('release in secs', release_t_in_secs)
# times to cut before and after video
min_pre_release = 10
min_post_release = 1

#min_pre_release = int(min_pre_release)
#min_post_release = int(min_post_release)

## trim videos before/after release
OutputDir = '/home/fponce/work/work_0629_videos/trimmed_videos'

for dirpath, dirnames, filenames in os.walk(DataDir):
	for filename in [f for f in filenames if f.endswith(".mp4") and experiment_date in f]:
		file_name = os.path.join(dirpath, filename)
		basename = os.path.basename(file_name)
		print(basename)
		bn =  basename[:basename.find(".mp4")]
		hour_start = int((basename.split('.')[0]).split('_')[-1][0:2])
		min_start = int((basename.split('.')[0]).split('_')[-1][2:4])
		sec_start = int((basename.split('.')[0]).split('_')[-1][4:6])
		vid_start_in_secs = (hour_start*3600+min_start*60+sec_start)
		#print(min_start)
		sec_start = release_t_in_secs - vid_start_in_secs - (min_pre_release)*60
		sec_end = release_t_in_secs - vid_start_in_secs + (min_pre_release + min_post_release)*60
		#sec_end = vid_start_in_secs + (min_pre_release + min_post_release)*60
		#print(sec_start, sec_end)
		splitx_string = str(sec_start) +":" + str(sec_end)
		output_name = bn +'_trimmed'+'.mp4'
		output_name = OutputDir+'/'+output_name
		call(["MP4Box", "-splitx", splitx_string, file_name, "-out", output_name])
		print('sliced', basename)


for dirpath, dirnames, filenames in os.walk(OutputDir):
	for filename in [f for f in filenames if f.endswith(".mp4")]:
		#print (os.path.join(dirpath, filename))
		file_name = os.path.join(dirpath, filename)
		basename = os.path.basename(file_name)
		#run SkyTracker
		basename_noext, dummy = os.path.splitext(basename)
		output_video_name = 'tracking_{0}.mp4'.format(basename_noext,t)
		blob_file_name = 'blob_data_{0}.txt'.format(basename_noext,t)
		output_video_name = 'tracking_'+basename_noext+'_'+t+'.mp4'
		blob_file_name = 'blob_data_'+basename_noext+'_'+t+'.txt'

		param = {
		'bg_window_size': 5,#3
		'fg_threshold': 5,
		'datetime_mask': {'x': 430, 'y': 15, 'w': 500, 'h': 40},
		'min_area': 2,
		'max_area': 20000,
		'open_kernel_size': (3,3),
		'close_kernel_size': (15,15),
		'output_video_name': output_video_name,
		'output_video_fps': 25.0,
		'blob_file_name': blob_file_name,
		'show_dev_images' : False,
		'min_interblob_spacing' : 2
		}
		print(file_name)
		tracker = SkyTracker(file_name, param=param)
		tracker.run()
