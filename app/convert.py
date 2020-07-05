import json as json
import pandas as pd
import datetime as dt

#DataFrame settings
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)

#Read JSON
data = pd.read_json(r'5k.json')

#This is where we convert our data. Version 1.0.0 _ 6/28/2020
#Time.
data['time_elapsed'] = data.timestamp.loc[1:] - data.timestamp.loc[0]
data['time_interval'] = data['timestamp'].diff()
data['time_interval_float'] = data['time_interval'] / dt.timedelta(seconds=1)

#Speed.
data['speed_mph'] = ((data['speed'] * 3.28084 * 3600) / 5280)
data['difference_in_speed_mph'] = data['speed_mph'].diff()
data['speed_kmh'] = ((data['speed'] * 3600) / 1000)
data['difference_in_speed_kmh'] = data['speed_kmh'].diff()
data['speed_meters_sec'] = data['speed']
data['speed_feet_sec'] = (data['speed'] * 3.28084)
data['pace_min_mile'] = (60 / data['speed_mph'])
data['pace_min_km'] = (60 / data['speed_kmh'])

#Distance.
data['distance_total_miles'] = (data['distance'] / 1609.344)
data['distance_total_km'] = (data['distance'] / 1000)
data['distance_interval_miles'] = (data['distance'].diff() * 3.28084 / 5280)
data['distance_interval_km'] = (data['distance'].diff() / 1000)

#Elevation and altitude.
data['elevation_meters'] = data['altitude']
data['elevation_feet'] = (data['altitude'] * 3.28084)

#Vertical and horizontal movement.
data['rise_meters'] = data['altitude'].diff()
data['rise_feet'] = (data['altitude'].diff() * 3.28084)
data['run_meters'] = data['distance'].diff()
data['run_feet'] = (data['distance'].diff() * 3.28084)

#Cadence.
data['real_cadence'] = (data['cadence'] * 2)
data['steps_per_second'] = (data['real_cadence'] / 60)
data['steps_per_interval'] = data['steps_per_second'] * data['time_interval_float']
data['stride_length'] = (data['run_meters'] / data['steps_per_interval'])
#average stride length printed below


#Predicted gradient.
data['gradient_%'] = (data['rise_feet'] / data['run_feet'] * 100)

total_rows = []
count = 0
for row in data['altitude'].iteritems() :
	count = count + 1
	#print(count)
	total_rows.append(count)

#Number of rows.
num_rows = float((max(total_rows)))

#maxhr = input('What age are you in years?')
#Heart rate
data['heart_rate'] = data['heart_rate']
data['hr_%'] = ((data['heart_rate'] / 194) * 100)
data['average_hr'] = (data['heart_rate'].sum() / num_rows)
percent_average_hr = ((data['average_hr'] / 194) * 100) #print below
average_stride_length = (data['stride_length'].sum() / num_rows)


#Replace inf and na values with 0.
#data = data[]

####
print(data)
print("Your average heart rate for this activity was", max(data['average_hr']),"bpm.")
print("Average percent of your maximum heart rate : ",  max(percent_average_hr), "%")
print("Your average stride length for this activity was",average_stride_length,"meters.")

#Export DataFrame
data.to_csv('convert.csv')



