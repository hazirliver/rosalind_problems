import numpy as np

seq = ""
dna_strings = []

with open("multifasta.fasta", "r") as mfasta:
    for line in mfasta:
        if line.startswith(">"):
            if seq != "":
                dna_strings.append(seq)
            seq = ""
            continue
        else:
            seq += line.strip()
    dna_strings.append(seq)

m = len(dna_strings)
n = len(dna_strings[0])

profile_mat = np.zeros((4, n), dtype=int)  # A C G T

for i in range(n):
    for j in range(m):
        if dna_strings[j][i] == "A":
            profile_mat[0][i] += 1
        if dna_strings[j][i] == "C":
            profile_mat[1][i] += 1
        if dna_strings[j][i] == "G":
            profile_mat[2][i] += 1
        if dna_strings[j][i] == "T":
            profile_mat[3][i] += 1

consensus_argmax = np.apply_along_axis(np.argmax, 0, profile_mat)
consensus_code = {0: "A", 1: "C", 2: "G", 3: "T"}
consensus_string = ""
for el in consensus_argmax:
    consensus_string += consensus_code[el]
print(consensus_string)

print("A: " + ' '.join(map(str, profile_mat[0])))
print("C: " + ' '.join(map(str, profile_mat[1])))
print("G: " + ' '.join(map(str, profile_mat[2])))
print("T: " + ' '.join(map(str, profile_mat[3])))
