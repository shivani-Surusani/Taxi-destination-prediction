#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cluster.py
import json
import hdbscan
import csv
import pandas as pd
import numpy
dests = []
Y=[]
def clust():
  df = pd.read_csv('taxi_data/train.csv', converters={'POLYLINE': lambda x: json.loads(x)[-1:]})
  
  for p in df['POLYLINE']:
     if len(p)>0:
     	dests.append([p[0][1], p[0][0]])
  pts = numpy.array(dests)
  clusterer = hdbscan.HDBSCAN(metric='euclidean',min_cluster_size=80)
  clusterer.fit(pts)
  #print clusterer.labels_.max()
  return clusterer.labels_
