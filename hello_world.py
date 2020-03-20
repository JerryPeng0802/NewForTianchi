import json
import pandas as pd
result = {
    "Q1": "Hello world",
    "Q2": 1,
    "Q3": [1]
}
df = pd.read_csv('/tcdata/num_list.csv', header=None)
# df = pd.read_csv('num.csv', header=None)
result['Q2'] = int(df.sum()[0])
x = list(df.sort_values(df.columns[0], ascending = False)[df.columns[0]].values[0: 10])
result['Q3'] = [int(a) for a in x]
print(result)
with open('result.json', 'w') as f:
    json.dump(result, f)
