#!/usr/bin/env python2
import numpy
import cPickle
import scipy.misc
import numpy as np
import pandas as pd
import json
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs
from itertools import cycle

import data


print "Generating Clusters"
df = pd.read_csv('taxi_data/train.csv', converters={'POLYLINE': lambda x: json.loads(x)[-1:]})
dests = []
for p in df['POLYLINE']:
   
   if len(p)>0:
   	dests.append([p[0][1], p[0][0]])
pts = numpy.array(dests)



bw = 0.001 


means = MeanShift(bandwidth=bw, bin_seeding=True, min_bin_freq=5)
means.fit(pts)
cluster_centers = means.cluster_centers_

print "Clusters shape: ", cluster_centers.shape
print cluster_centers



