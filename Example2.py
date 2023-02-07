import json
import pandas as pd
def export_to_csv():
    with open ('bcbstn.json') as f:
        data=json.loads(f.read())
        parser(data)
def parser(data):
    str_output=[]
    int_ouptut=[]
    for i in data.keys():
        if isinstance(data[i], str):
            str_output.append(data[i])
        if isinstance(data[i],int):
            int_ouptut.append(data[i])
        if isinstance(data[i],list): 
           list_parser(data[i],data,str_output,int_ouptut)

    print(str_output)
    print(int_ouptut)
def list_parser(items,data,str_output,int_ouptut):
    for val in items:
        for key_val in val.keys():
            if isinstance(val[key_val], str):
                str_output.append(val[key_val])
            if isinstance(val[key_val],int):
                int_ouptut.append(val[key_val])
            if isinstance(val[key_val],list): 
                list_parser(val[key_val],data,str_output,int_ouptut)






export_to_csv()