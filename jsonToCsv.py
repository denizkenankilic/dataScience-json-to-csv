# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:19:02 2021

@author: deniz.kilic
"""

import os
import json
import csv

def read_json(json_path, json_file):
    with open(os.path.join(json_path, json_file)) as f:
        data = json.load(f)
    f.close()
    return data

def json_to_csv(jsonGtPath, imageFormat, width, height, gtClass, filename):

    jsonNames = os.listdir(jsonGtPath)

    with open(filename, 'w', newline='') as csvfile:
         fields = ['filename','width','height','class','xmin','ymin','xmax','ymax']
         csvwriter = csv.DictWriter(csvfile, fieldnames=fields)

         csvwriter.writeheader()
         for json_file in jsonNames:
              file_name, file_extension = os.path.splitext(json_file)
              json_data = read_json(jsonGtPath, json_file)
              gt_samples = json_data['samples']
              for sample in gt_samples:
                  #class_num = str(sample['class'])
                  #idx_num = str(sample['idx'])
                  #modified = str(sample['isModified'])
                  x_min = int(float(sample['x_min']))
                  y_min = int(float(sample['y_min']))
                  x_max = int(float(sample['x_max']))
                  y_max = int(float(sample['y_max']))

                  csvwriter.writerow({'filename': file_name + '.' + imageFormat, 'width': width,
                                      'height': height, 'class': gtClass, 'xmin': x_min,
                                      'ymin': y_min, 'xmax': x_max, 'ymax': y_max})

# Result path for json files
jsonGtPath = r'updated_gts_AOI_02_tile_1024' # Edit json ground truths path
imageFormat = 'jpg' # Edit image format
width = '1024' # edit width of tiles
height = '1024' # edit height of tiles
gtClass = 'track' # Edit class of ground truth
filename = "jsonToCsv.csv" # Edit file name for csv
# inputs are variables that "finetune_detection.py" creates in pickle folder
json_to_csv(jsonGtPath)
