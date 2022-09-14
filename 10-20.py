import pandas as pd

data = pd.read_csv("C:/Users/ashni/OneDrive/Desktop/py4e/Biox/second_sort_length_mol-wt.csv")

Mol_wt = data["Molecular weight"]
cds = data["coding sequence"]
unique_code = data["unique code"]

u_c = []
filter_data = []
for i in range(len(unique_code)):
    if Mol_wt[i] >= 10000 and Mol_wt[i] <= 20000:
        filter_data.append(cds[i])
        u_c.append(unique_code[i])

print(filter_data)
print(len(filter_data))

print(len(u_c))

dictionary = {"Unique code": u_c, "sorted amino acids": filter_data}

df = pd.DataFrame(dictionary)

df.to_csv("10-20.csv")
