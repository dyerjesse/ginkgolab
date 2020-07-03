import csv
import json

with open('convert.csv') as csvfile :
	readCSV = csv.reader(csvfile, delimiter=',')
	#Create a dictionary for the data.
	index = []
	altitude = []
	distance = []
	enhanced_altitude = []
	enhanced_speed = []
	heart_rate = []
	position_lat = []
	position_long = []
	speed = []
	timestamp = []
	unknown = []
	time_elapsed = []
	time_interval = []
	speed_mph = []
	difference_in_speed_mph = []
	speed_kmh = []
	speed_meters_sec = []
	speed_feet_sec = []
	pace_min_mile = []
	pace_min_km = []
	distance_total_miles = []
	distance_total_km = []
	distance_interval_miles = []
	distance_interval_km = []
	elevation_meters = []
	elevation_feet = []
	rise_meters = []
	rise_feet = []
	run_meters = []
	run_feet = []
	percent_gradient = []
	percent_maxhr = []
	print(altitude)

	#Read the data values.
	for row in readCSV:
		index = [0]
		altitude = [1]
		distance = [2]
		enhanced_altitude = [3]
		enhanced_speed = [4]
		heart_rate = [5]
		position_lat = [6]
		position_long = [7]
		speed = [8]
		timestamp = [9]
		unknown = [10]
		time_elapsed = [11]
		time_interval = [12]
		speed_mph = [13]
		difference_in_speed_mph = [14]
		speed_kmh = [15]
		speed_meters_sec = [16]
		speed_feet_sec = [17]
		pace_min_mile = [18]
		pace_min_km = [19]
		distance_total_miles = [20]
		distance_total_km = [21]
		distance_interval_miles = [22]
		distance_interval_km = [23]
		elevation_meters = [24]
		elevation_feet = [25]
		rise_meters = [26]
		rise_feet = [27]
		run_meters = [28]
		run_feet = [29]
		percent_gradient = [30]
		percent_maxhr = [31]

		'''#Replace the blank dictionary outside of the loop with the new values.
		index.append(index)
		altitude.append(altitude)
		distance.append(distance)
		enhanced_altitude.append(enhanced_altitude)
		enhanced_speed.append(enhanced_speed)
		heart_rate.append(heart_rate)
		position_lat.append(position_lat)
		position_long.append(position_long)
		speed.append(speed)
		timestamp.append(timestamp)
		unknown.append(unknown)
		time_elapsed.append(time_elapsed)
		time_interval.append(time_interval)
		speed_mph.append(speed_mph)
		difference_in_speed_mph.append(difference_in_speed_mph)
		speed_kmh.append(speed_kmh)
		speed_meters_sec.append(speed_meters_sec)
		speed_feet_sec.append(speed_feet_sec)
		pace_min_mile.append(pace_min_mile)
		pace_min_km.append(pace_min_km)
		distance_total_miles.append(distance_total_miles)
		distance_total_km.append(distance_total_km)
		distance_interval_miles.append(distance_interval_miles)
		distance_interval_km.append(distance_interval_km)
		elevation_meters.append(elevation_meters)
		elevation_feet.append(elevation_feet)
		rise_meters.append(rise_meters)
		rise_feet.append(rise_feet)
		run_meters.append(run_meters)
		run_feet.append(run_feet)
		percent_gradient.append(percent_gradient)
		percent_maxhr.append(percent_maxhr)'''

		print(distance)
