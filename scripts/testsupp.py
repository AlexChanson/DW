import spotipy
import sys
import pprint
import spotipy
import spotipy.util as util
import json
import csv
from datetime import datetime, timedelta, date

#Parameterage
infile = "data/data.csv"
outfile = "data/cleandata.csv"
separator = ","
separateur = ";"
header = True

with open(infile, encoding='utf8') as f:
    lines = csv.reader(f, delimiter=separator)
    with open(outfile,encoding='utf8', mode="w") as out:
        next(lines)
        for line in lines:
            if header:
                header = False
                #out.write(separateur.join(line) + "\n")
                out.write(line[1] + separateur + line[2] + separateur + line[len(line) - 5] + separateur + line[
                    len(line) - 4] + separateur + line[len(line) - 3] + separateur + line[len(line) - 2] + separateur +
                          line[len(line) - 1])
                out.write("\n")
            else:
                if str(line[1]) != "Position":
                    out.write(line[1] + separateur + line[2] + separateur + line[len(line)-5] + separateur + line[len(line)-4] + separateur + line[len(line)-3] + separateur + line[len(line)-2] + separateur + line[len(line)-1])
                    out.write("\n")