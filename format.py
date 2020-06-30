import json as json

with open ('con.json', 'r') as f :
	data = [json.loads(f) for line in open('con.json', 'r')]
	print(read)
