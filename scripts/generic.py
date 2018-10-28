def action(input):
    d = int(input[0]) + int(input[1])
    return [str(d)]


# Debut du script
import csv

# Parameterage
infile = "test.csv"
outfile = "test_mod.csv"
separateur = ","
header = True

with open(infile) as f:
    # Open the input file
    lines = csv.reader(f, delimiter=separateur)
    with open(outfile, mode="w") as out:
        # for each row
        for line in lines:
            # if there is a header ignore it and copy it over the output file
            if header:
                header = False
                out.write(separateur.join(line) + "\n")
            # else pass the row to the mapper and append the result
            else:
                result = action(line)
                out.write(separateur.join(line))
                for item in result:
                    out.write(separateur + item)
                out.write("\n")
