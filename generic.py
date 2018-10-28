def action(input):
	d = int(input[0]) + int(input[1])
	return [str(d)]




#Debut du script
import csv

#Parameterage
infile = "test.csv"
outfile = "test_mod.csv"
separateur = ","
header = True

with open(infile) as f:
	lines = csv.reader(f, delimiter=separateur)
	with open(outfile, mode="w") as out:
		for line in lines:
			if header:
				header = False
				out.write(separateur.join(line) + "\n")
			else:
				result = action(line)
				out.write(separateur.join(line))
				for item in result:
					out.write(separateur + item)
				out.write("\n")