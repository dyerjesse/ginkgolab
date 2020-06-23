import json
#import pandas as pd

json_data = '{"altitude" : 1, "distance" : 2, "enhanced_altitude" : 3, "enhanced_speed" : 4, "heart_rate" : 5, "position_lat" : 6, "position_long" : 7, "speed" : 8, "timestamp" : 9, "activity" : 10}'
parsed_json = (json.loads(json_data))
print(json.dumps(parsed_json, indent = 4, sort_keys=True))

with open ("MoodyRancher.json", 'r') as df:
	moodyrancher_dict = json.load(df)

for moodyrancher in moodyrancher_dict:
	speedMph = float(moodyrancher['speed']) * 3.28084 * 3600 / 5280
	if speedMph > 20:
		print(moodyrancher['timestamp'])
		print(speedMph)
		print(moodyrancher['heart_rate'])
