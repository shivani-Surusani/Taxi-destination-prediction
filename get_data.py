#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  get_data.py
import json
import csv
import numpy as np
import pandas as pd
import pickle
from sklearn import preprocessing
'''with open('taxi_data/train.csv','r') as dfile:
	reader=csv.reader(dfile,delimiter=",")
data=list(reader)
	print data[0]
	data.remove(data[0])'''
Trip_ind={}
m_data={'trip_id':[],'call_type':[],'origin_call':[],'origin_stand':[],'taxi_id':[],'time_stamp':[]}#meta data
with open('taxi_data/train.csv','r') as dfile:
  reader=csv.reader(dfile,delimiter=",")
  data=list(reader)
  data.remove(data[0])
c=0
for ind,i in enumerate(data):
  Trip_ind[i[0]]=c
  c=c+1
  m_data['trip_id'].append(i[0])
  m_data['call_type'].append(i[1])
  m_data['origin_call'].append(i[2])
  m_data['origin_stand'].append(i[3])
  m_data['taxi_id'].append(i[4])
  m_data['time_stamp'].append(i[5])
gps_data= pd.read_csv('taxi_data/test.csv',usecols=['POLYLINE'],converters={'POLYLINE': lambda x: json.loads(x)})
latlon=[]
trip_ll=[]
for path in gps_data['POLYLINE']:
	latlon.append([(lat,lon)for lon, lat in path if len(path)>0])
	#print len(path)
latlon1=np.array(latlon)
taxi_loc={}
with open('taxi_data/metaData_taxistandsID_name_GPSlocation.csv','r') as dfile1:
  reader=csv.reader(dfile1,delimiter=",")
  data1=list(reader)
  data1.remove(data1[0])
taxi_loc={'taxi_id':[]}
for index,ii in enumerate(data1):
  taxi_loc[ii[0]]=[]
  taxi_loc[ii[0]].append(i[2])
  taxi_loc[ii[0]].append(i[3])
#normalizing the latlon
'''for ll in latlon1:
  latlon_norm=preprocessing.normalize(ll,axis=1)'''
pickl_trip_ind = open("pickl_trip_ind.pickle","wb")
pickle.dump(Trip_ind, pickl_trip_ind)
pickling_on.close()
pickl_m_data = open("pickl_m_data.pickle","wb")
pickle.dump(m_data, pickl_m_data)
pickling_on.close()
pickl_latlon = open("pickl_latlon.pickle","wb")
pickle.dump(latlon1, pickl_latlon)
pickling_on.close()


                       

