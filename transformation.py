#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  transformation.py
# 
pickl_trip_ind = open("pickl_trip_ind.pickle","rb")
trip_ind= pickle.load(pickle_off)
pickl_m_data = open("pickl_m_data.pickle","rb")
m_data= pickle.load(pickl_m_data)
pickl_latlon = open("pickl_latlon.pickle","rb")
latlon= pickle.load(pickl_latlon)
X=[]
def taxi_add_first_last_lon_lat():
  for ind,row in latlon:
    ff_lats=list(row[0:6,0])
    norm_f_lat=[numpy.float32(i)/sum(ff_lats) for i in list(row[0:6,0])]
    norm_f_lon=[numpy.float32(i)/sum(ff_lats) for i in list(row[0:6,0])]
    norm_l_lat=[numpy.float32(i)/sum(ff_lats) for i in list(row[0:6,0])]
    norm_l_lon=[numpy.float32(i)/sum(ff_lats) for i in list(row[0:6,0])]
    
    X.append(norm_f_lat+norm_f_lon+norm_l_lat+norm_l_lon)
def date_time():
  for ind,mm m_data['time_stamp']:
    dt = datetime.datetime.utcfromtimestamp(mm)
    yearweek = dt.isocalendar()[1] - 1
    wy=numpy.int8(51 if yearweek == 52 else yearweek)
    dw=numpy.int8(dt.weekday()
    hd=numpy.int8(dt.hour * 4 + dt.minute / 15))
    caller_id=numpy.int32(m_data['origin_call'][ind])
    stand_id=numpy.int32(m_data['origin_stand'][ind])
    taxi_id=numpy.int32(m_data['taxi_id'][ind])
    X[ind].append(wy)
    X[ind].append(dw)
    X[ind].append(hd)
    X[ind].append(caller_id)
    X[ind].append(stand_id)
    X[ind].append(taxi_id)
def transform():
  return X   