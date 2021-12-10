# Demand
# http://mis.nyiso.com/public/P-58Clist.htm

import urllib3
import pandas as pd
from pandas import DataFrame as df
import io
from io import BytesIO
import zipfile

#I used url library manager instead of beautiful soup and seemed to work
#do not need a start and end date can GET by months once avaliable or days of the current month
http = urllib3.PoolManager()

#this function is for getting a single day from this month
def demand(x, y):
    # x is the type of data
    r = http.request('GET', 'http://mis.nyiso.com/public/csv/'+x+'/'+ y+x+'.csv')
    bytes_data = r.data
    demand = pd.read_csv(BytesIO(bytes_data))
    print(demand.head)

#this function is only for previous months of data that come in zipped format
def demandZip(x, y):
    r = http.request('GET', 'http://mis.nyiso.com/public/csv/'+x+'/'+ y+x+'_csv.zip')
    bytes_data = r.data
    immutable_bytes = bytes(bytes_data)
    #create file to unzip
    with open("my_file.zip", "wb") as binary_file:
        binary_file.write(immutable_bytes)
    with zipfile.ZipFile("my_file.zip", 'r') as zip_ref:
        zip_ref.extractall(".")
    demand = pd.read_csv(y+x+".csv")
    print(demand.head)
    

x1 = 'palIntegrated' # or isolf
y1 = '20201101'
demandZip(x1, y1)
