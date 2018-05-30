
import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# reading training data
df = pd.read_csv('taxi_data/train.csv', converters={'POLYLINE': lambda x: json.loads(x)[-1:]})
ll=[]
temp=[]
for p in df['POLYLINE']:
	if len(p)>0:
		ll.append([p[0][1], p[0][0]])
latlong=np.array(ll)
print latlong.shape
# cut off long distance trips
latitude_low, latitude_hgh = np.percentile(latlong[:,0], [2, 98])
longitude_low, longitude_hgh = np.percentile(latlong[:,1], [2, 98])

# create image
bins = 510
lat_bins = np.linspace(latitude_low, latitude_hgh, bins)
lon_bins = np.linspace(longitude_low, longitude_hgh, bins)
H2, _, _ = np.histogram2d(latlong[:,0], latlong[:,1], bins=(lat_bins, lon_bins))

img = np.log(H2[::-1, :] + 0)

plt.figure()
ax = plt.subplot(1,1,1)
plt.imshow(img)
plt.axis('off')
plt.title('end points')
plt.savefig("taxi_trip_end_points.png")

