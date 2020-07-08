import json as json
import pandas as pd
import datetime as dt
from operator import truediv

#DataFrame settings
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)

#Read JSON
data = pd.read_json(r'gcloopbike.json')

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
if 'cadence' in data:
	print("Cadence was recorded for this activity.")
	data['real_cadence'] = (data['cadence'] * 2)
	data['steps_per_second'] = (data['real_cadence'] / 60)
	data['steps_per_interval'] = data['steps_per_second'] * data['time_interval_float']
	data['stride_length'] = (data['run_meters'] / data['steps_per_interval'])
#Average stride length printed below.
else:
	print("No cadence was recorded for this activity.")

#Calculate total number of rows.
total_rows = []
count = 0
for row in data['altitude'].iteritems() :
	count = count + 1
	total_rows.append(count)
num_rows = float((max(total_rows)))

#Heart rate
data['heart_rate'] = data['heart_rate']
data['hr_%'] = ((data['heart_rate'] / 194) * 100)
data['average_hr'] = (data['heart_rate'].sum() / num_rows)

#Calculate average hr.
percent_average_hr = ((data['average_hr'] / 194) * 100) #print below

#Calculate average stride length.


#Calculate total number of rows.
total_rows = []
count = 0
for row in data['altitude'].iteritems() :
	count = count + 1
	total_rows.append(count)
num_rows = float((max(total_rows)))

#Calculate total ascent.
total_gain = []
gain = 0
for row, value in data['rise_meters'].iteritems():
	if value > 0 :
		gain = gain + value
		total_gain.append(gain)
total_evelvation_gain = (max(total_gain))

#Calculate total descent.
total_descent = []
descent = 0
for row, value in data['rise_meters'].iteritems():
	if value < 0 :
		descent = descent + value
		total_descent.append(descent)
total_evelvation_loss = (min(total_descent))

#Calculate total elevation change.
total_elevation_change = data['altitude'].max() - data['altitude'].min()

#Calculate gradient.
data['run_feet'].fillna(0, inplace=True)
data['rise_feet'].fillna(0, inplace=True)

rise_ten_interval = []
run_ten_interval = []
rise_count = 0.1
run_count = 0.1

for row, value in data['rise_feet'].iteritems():
	rise_count = rise_count + value
	if row % 1 == 0:
		rise_ten_interval.append(rise_count)
		#rise_ten_interval.append(0.001)
		rise_count = 0.1

for row, value in data['run_feet'].iteritems():
	run_count = run_count + value
	if row % 1 == 0:
		run_ten_interval.append(run_count)
		#run_ten_interval.append(.001)
		run_count = 0.1

gradient = list(map(truediv, rise_ten_interval, run_ten_interval))
data['gradient_%'] = gradient
data['gradient_%'] = data['gradient_%'] * 100
data['gradient_%'] = data['gradient_%'].replace(100, "na")

#Print datatypes
print(data.dtypes)		
####
print(data)
print("Your average heart rate for this activity was", max(data['average_hr']),"bpm.")
print("Average percent of your maximum heart rate : ",  max(percent_average_hr), "%")
print("Your total ascent during this activity was",total_evelvation_gain,"meters.")
print("Your total descent during this activity was",total_evelvation_loss,"meters.")
print("Your total elevation change during this activity was",total_elevation_change,"meters.")

#Calculate and print average stride length.
if 'stride_length' in data:
	average_stride_length = (data['stride_length'].sum() / num_rows) #print below
	print("Your average stride length for this activity was",average_stride_length,"meters.")
else :
	print("There is no stride length data.")

#Scoring starts. V1.0.0 7/8/2020
data['heart_rate'].fillna(0, inplace=True)

print(data['heart_rate'].max(), "Highest heart rate achieved.")
print(data['heart_rate'].median(), "Median heart rate.")
print(data['heart_rate'].min(), "Lowest heart rate.")
print(data['heart_rate'].max() - data['heart_rate'].min(), "Difference between max and min heart rate.")

hr_log = []
hr_progress = 0
hr_count = 0
hr_hold = data['heart_rate'].iloc[0]
print(hr_hold)

for row, value in data['heart_rate'].iteritems():
	if value >= hr_progress:
		hr_hold = hr_progress
		hr_progress = value
		hr_count = hr_count + 1
		print(hr_hold, hr_progress, hr_count)
	else :
		hr_log.append(hr_progress)
		hr_log.append(hr_count)
print(hr_log)		
print(hr_progress)

		



#Export DataFrame
data.to_csv('convert.csv')
##END##