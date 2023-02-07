import json
import pandas as pd
def export_to_csv():
    with open ('bcbstn.json') as f:
        data=json.loads(f.read())
        output=[]
        for i in range(0,len(data)):
            temp=[]
            for value in data[i]:
                temp.append(data[i][value])
            output.append(temp)
        df = pd.DataFrame(output,columns=get_header(data[0]))
        df.to_csv(index=False)
def get_header(items):
    return list(items.keys())
export_to_csv()