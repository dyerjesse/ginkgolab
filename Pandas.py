import json as json
import pandas as pd
pd.set_option('display.max_rows', 1000)

data = pd.read_json(r'MoodyRancher.json')
data_format = {"altitude" : 1, "distance" : 2, "heart_rate" : 3, "speed" : 4, "timestamp" : 5}
print(data)

def miles_per_hour (dist, speed) :
	speed_in_feet = data['speed'] * 3.28084 * 3600
	speed_in_mph = speed_in_feet / 5280
	return speed_in_mph
print(miles_per_hour(0,0))

# This is where we calulate % gradient during each interval
for row, value in data['altitude'].iteritems():
	print (row, value)
data['rise'] = data['altitude'].diff() * 3.28084
data['run'] = data['distance'].diff() * 5280
data['gradient'] = data['rise'] / data['run'] * 100
for row, value in data['gradient'].iteritems():
	print(row, value)
print data['gradient']







print data
	