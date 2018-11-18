import sys
import csv
import logging
import progressbar

progressbar.streams.wrap_stderr()
logging.basicConfig()


if len(sys.argv) < 4:
    print("Use final.py infile.csv outfile.csv out_errors.csv")
    sys.exit(1)

############################
#       Parameterage       #
############################
infile = sys.argv[1]
outfile = sys.argv[2]
errfile = sys.argv[3]
separateur = ";"
header = True


with open(infile, encoding='utf8') as f:
    lines = csv.reader(f, delimiter=separateur)
    with open(outfile, encoding='utf8', mode="w") as out:
        with open(outfile, encoding='utf8', mode='w') as err:
            for line in progressbar.progressbar(lines):
                if header:
                    header = False
                    out.write(separateur.join(line) + "\n")
                else:
                    try:
                        if line[1] == "" or line[2] == "" or line[11] == "":
                            line[1] = "DELETED"
                            line[2] = "DELETED"
                            line[3] = "DELETED"
                        flag = False
                        for item in line:
                            if item == "":
                                flag = True
                        if flag:
                            out.write(separateur.join(line) + "\n")
                        else:
                            err.write(separateur.join(line) + "\n")
                    except IndexError:
                        err.write(separateur.join(line) + "\n")


