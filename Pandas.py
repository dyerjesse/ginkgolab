import json as json
import pandas as pd

gradient = ()
data = pd.read_json(r'MoodyRancher.json')
data_format = {"altitude" : 1, "distance" : 2, "heart_rate" : 3, "speed" : 4, "timestamp" : 5}

rise = (data.loc[1, 'altitude'] * 3.2 - data.loc[0, 'altitude'] * 3.2) * 100
run = data.loc[1, 'distance'] * 5280 - data.loc[0, 'distance'] * 5280

gradient = rise / run
#print data
print "gradient = ", gradient

for diff, row in data.iterrows():
	data.loc[diff, "Rise"] = row['altitude'] - row['distance']

print diff
