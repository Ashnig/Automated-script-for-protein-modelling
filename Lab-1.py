#Program for reading FASTA files

input_file = open("uniprot.txt", "r")
ac_list = []
for line in input_file:
    if line[0] == ">":
        fields = line.split("|")
        ac_list.append(fields[1])

print(ac_list)


#How to parse genbank sequence records
Input = open("covid.gbk")
Output = open("covid.fasta", "w")

f = 0
for line in Input:
    if line[0:9] == "ACCESSION":
        AC = line.split()[1].strip()
        #Output.write(">" + AC + "\n")
    elif line[0:6] == "ORIGIN":
        f = 1
    elif f == 1:
        fields = line.split()
        if fields != []:
            seq = "".join(fields[1:])
            Output.write(seq.upper() + "\n")
Input.close()
Output.close()
