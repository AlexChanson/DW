import glob
import os
import pandas as pd
from datetime import datetime, timedelta, date


df=pd.DataFrame()
for file_ in os.listdir("data"):
    temp=pd.read_csv("data"+'/'+file_,header=None,skiprows=1)
    df=pd.concat([df,temp],ignore_index=True)
#df.columns=["Position","Track Name","Artist","Streams","URL","Date","Country"]
df.to_csv("data/"+'data.csv',index=False)