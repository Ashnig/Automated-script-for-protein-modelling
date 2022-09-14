#if condition
#amino acids should be > 90 and < 182

import pandas as pd

data = pd.read_csv("C:/Users/ashni/OneDrive/Desktop/py4e/Biox/10-20.csv")
cds = data["sorted amino acids"]

#calculating length
length = []
for i in range(len(cds)):
    length.append(cds.str.len()[i])

#putting the length of each cds in another column
data["Length"] = length

#calculating molecular weight
Mol_wt = []
for i in range(len(length)):
    Mol_wt.append(length[i]*110)

#putting the molecular weight of each cds in another column
data["Molecular weight"] = Mol_wt

#Saving this whole thing in another csv
data.to_csv("10-20_mol_wt.csv")
