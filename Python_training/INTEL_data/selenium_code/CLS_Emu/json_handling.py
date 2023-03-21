import pandas as pd
import json

'''f= open('result.json')
data = f.read()
f.close()
#print(data)

data = data.replace('[','\'{')
data = data.replace(']','}\'')
#res = json.loads(data)
print(data)'''

import pandas as pd

df = pd.read_json('result.json')

#print(df.to_string())
df.to_excel('result.xlsx')