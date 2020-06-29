import json as json
import pandas as pd

#DataFrame settings
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 50)

#Read JSON
data = pd.read_json(r'MoodyRancher.json')

#This is where we convert our data. Version 1.0.0 _ 6/28/2020
#Time.
data['time_elapsed'] = data.timestamp.loc[1:] - data.timestamp.loc[0]
data['time_interval'] = data['timestamp'].diff()

#Speed.
data['speed(mph)'] = ((data['speed'] * 3.28084 * 3600) / 5280)
data['difference in speed(mph)'] = data['speed(mph)'].diff()
data['speed(km/h)'] = ((data['speed'] * 3600) / 1000)
data['difference in speed(km/h)'] = data['speed(km/h)'].diff()
data['speed(meters/sec)'] = data['speed']
data['speed(feet/sec)'] = (data['speed'] * 3.28084)
data['pace(min/mile)'] = (60 / data['speed(mph)'])
data['pace(min/km)'] = (60 / data['speed(km/h)'])

#Distance.
data['distance_total(miles)'] = (data['distance'] / 1609.344)
data['distance_total(km)'] = (data['distance'] / 1000)
data['distance_interval(miles)'] = (data['distance'].diff() * 3.28084 / 5280)
data['distance_interval(km)'] = (data['distance'].diff() / 1000)

#Elevation and altitude.
data['elevation(meters)'] = data['altitude']
data['elevation(feet)'] = (data['altitude'] * 3.28084)

#Vertical and horizontal movement.
data['rise(meters)'] = data['altitude'].diff()
data['rise(feet)'] = (data['altitude'].diff() * 3.28084)
data['run(meters)'] = data['distance'].diff()
data['run(feet)'] = (data['distance'].diff() * 3.28084)

#Predicted gradient.
data['gradient(%)'] = (data['rise(feet)'] / data['run(feet)'] * 100)

#maxhr = input('What age are you in years?')
#Heart rate
data['heart rate'] = data['heart_rate']
data['hr(%)'] = ((data['heart_rate'] / 194) * 100)

#Print DataFrame
print data	