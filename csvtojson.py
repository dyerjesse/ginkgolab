import pandas as pd
df = pd.read_csv (r'con.csv')
df.to_json (r'con.json')