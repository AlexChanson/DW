import os
import subprocess
from datetime import datetime, timedelta, date
import glob

files = glob.glob('data/*')

for f in files:
    os.remove(f)

startdate = str((datetime.now() - timedelta(days=12)).date())
enddate = str((datetime.now() - timedelta(days=7)).date())
regions = ["global", "us", "gb", "ad", "ar", "at", "au", "be", "bg",
               "bo", "br", "ca", "ch", "cl", "co", "cr", "cy", "cz", "de",
               "dk", "do", "ec", "ee", "es", "fi", "fr", "gr", "gt", "hk",
               "hn", "hu", "id", "ie", "is", "it", "jp", "lt", "lu", "lv",
               "mc", "mt", "mx", "my", "ni", "nl", "no", "nz", "pa", "pe",
               "ph", "pl", "pt", "py", "se", "sg", "sk", "sv", "tr", "tw", "uy"]

for region in regions:
    subprocess.call("python3 charts.py --start_date "+startdate+" --outfile data/"+region+".csv --end_date "+enddate+" --region "+region+" --freq weekly --chart top200", shell=True)


subprocess.call("python3 mergecsv.py" , shell=True)
subprocess.call("python3 testsupp.py" , shell=True)
subprocess.call("python3 -m addattributes data/cleandata.csv finalweekdata.csv err.csv" , shell=True)
