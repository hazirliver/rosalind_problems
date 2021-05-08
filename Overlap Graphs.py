dna_strings = {}
gene = ""

with open("multifasta.fasta", "r") as fasta:
    for line in fasta:
        if line.startswith(">"):
            if gene != "":
                dna_strings[id] = gene
            id = line.strip()[1:]
            gene = ""
        if not line.startswith(">"):
            gene += line.strip()
    dna_strings[id] = gene


def is_overlap(s1, s2, k):
    return (s1[:k] == s2[-k:])


for i, key1 in enumerate(dna_strings):
    for j, key2 in enumerate(dna_strings):
        if j != i:
            if dna_strings[key1][-3:] == dna_strings[key2][:3]:
                print(key1 + " " + key2)
