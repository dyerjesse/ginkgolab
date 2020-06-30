import json as json
import pandas as pd

#DataFrame settings
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 50)

#Read JSON
data = pd.read_json(r'MoodyRancher.json')

#This is where we convert our data. Version 1.0.0 _ 6/28/2020
#Time.
data['time_elapsed'] = data.timestamp.loc[1:] - data.timestamp.loc[0]
data['time_interval'] = data['timestamp'].diff()

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

#Predicted gradient.
data['gradient_%'] = (data['rise_feet'] / data['run_feet'] * 100)

#maxhr = input('What age are you in years?')
#Heart rate
data['heart_rate'] = data['heart_rate']
data['hr_%'] = ((data['heart_rate'] / 194) * 100)

#Print DataFrame
print data
#Export DataFrame
#data.to_json('con.json', orient='records', lines=True)
data.to_csv('con.csv')



