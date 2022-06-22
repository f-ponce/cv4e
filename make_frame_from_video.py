#!/usr/bin/env python3
import warnings
import numpy as np
import os
import time
from subprocess import call
import cv2
###############################################################################

# experiment_dates = ['0629']
# DataDir = '/Volumes/COMPA/upward_facing_cameras_data/pre_processed_data'
# DataDir = '/Volumes/COMPA/upward_facing_cameras_data/pre_processed_data/pre_processed_data_0629/ufc_20_01_vi_0001_20190629_171133_trimmed.mp4'
# Outdir = '/Volumes/COMPA/upward_facing_cameras_data/pre_processed_data/pre_processed_data_0629/frames_ufc_20_01_vi_0001_20190629_171133/'

experiment_dates = ['0611']
DataDir = '/Volumes/COMPA/upward_facing_cameras_data/pre_processed_data'
DataDir = '/Volumes/COMPA/upward_facing_cameras_data/pre_processed_data/pre_processed_data_0611/ufc_01_vi_0000_20190611_062021_trimmed.mp4'
Outdir = '/Volumes/COMPA/upward_facing_cameras_data/pre_processed_data/pre_processed_data_0611/frames_ufc_01_vi_0000_20190611_062021/'

vidcap = cv2.VideoCapture(DataDir)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(Outdir+'frame%d.jpg' % count, image)# save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success, count)
  count += 1
