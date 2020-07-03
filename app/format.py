import csv
import json

csvfile = open('convert.csv', 'r')
jsonfile = open ('toJson.json', 'w')

fieldnames = ("index" : 0, "altitude", "distance", "enchanced_altitude", "enchanced_speed",
 			"heart_rate", "position_lat", "position_long", "speed", "timestamp", "unknown_88",
 			"time_elapsed", "time_interval", "speed_mph", "difference_in_speed_mph", "speed_kmh",
 			"difference_in_speed_kmh", "speed_meters_sec", "speed_feet_sec", "pace_min_mile",
 			"pace_min_km", "distance_total_miles", "distance_total_km", "elevation_meters"
 			"elevation_feet", "rise_meters", "rise_feet", "run_meters", "run_feet", "gradient_%",
 			"hr_%")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader :
	json.dump(row, jsonfile)
	jsonfile.write('\n')

print(jsonfile)