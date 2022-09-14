import pandas as pd
import csv


file = open("Taenia_solium.txt", "r")
out_file = open("trial_output.txt", "w")
seq = ""
#li means the particular name of the protein sequence
li = []
cds = []
for line in file:
    if line[0] == ">":
        header = line[1:14]
        li.append(header)
    elif line[0] == ">" and seq == "":
        #process the first line of the input file
        header = line
        li.append(header)
    elif line[0] != ">":
    #join the lines with sequence
        seq = seq + line
        cds.append(line)
    elif line[0] == ">" and seq != "":
    #in subsequent lines starting with ">"
    #write the previous header and sequence to the output file.
    #then re-initialize the header and
    #seq variables for the next record
        if "TsM" in header:
            out_file.write(header + seq)
        seq = ""
        header = line
    #take care of the very last record of the input file
if "TsM" in header:
    out_file.write(header + seq)


print(len(cds))
print(len(li))

#saving to the dataframe
dict = {"unique code": li, "coding sequence": cds}

df = pd.DataFrame(dict)

df.to_csv("first_sort_text_to_sheet.csv")








out_file.close()
