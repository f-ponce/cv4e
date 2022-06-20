#!/usr/bin/env python3
import time
import numpy
from subprocess import call
import os.path
import datetime
import sys
import skytracker

#convert videos from h264 to mp4

# input raw video directory
DataDir = '/home/fponce/field_data_0629'
t = time.strftime("%Y%m%d_%H%M%S", time.localtime())\

#output videos directory
DataDir_out = '/home/fponce/work/work_0629_videos'

# find all videos in the main experiment folder and convert them to .mp4

for dirpath, dirnames, filenames in os.walk(DataDir):
	for filename in [f for f in filenames if f.endswith(".mp4.h264")]:
		file_name = os.path.join(dirpath, filename)
		output_name = os.path.join(dirpath,filename+'converted.mp4')
		print (os.path.join(dirpath, filename))
		call(["MP4Box", "-add", file_name, output_name])

######################################################################################
