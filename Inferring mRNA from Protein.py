rna_codon_table = {"UUU": "F",
                   "CUU": "L",
                   "AUU": "I",
                   "GUU": "V",
                   "UUC": "F",
                   "CUC": "L",
                   "AUC": "I",
                   "GUC": "V",
                   "UUA": "L",
                   "CUA": "L",
                   "AUA": "I",
                   "GUA": "V",
                   "UUG": "L",
                   "CUG": "L",
                   "AUG": "M",
                   "GUG": "V",
                   "UCU": "S",
                   "CCU": "P",
                   "ACU": "T",
                   "GCU": "A",
                   "UCC": "S",
                   "CCC": "P",
                   "ACC": "T",
                   "GCC": "A",
                   "UCA": "S",
                   "CCA": "P",
                   "ACA": "T",
                   "GCA": "A",
                   "UCG": "S",
                   "CCG": "P",
                   "ACG": "T",
                   "GCG": "A",
                   "UAU": "Y",
                   "CAU": "H",
                   "AAU": "N",
                   "GAU": "D",
                   "UAC": "Y",
                   "CAC": "H",
                   "AAC": "N",
                   "GAC": "D",
                   "UAA": "Stop",
                   "CAA": "Q",
                   "AAA": "K",
                   "GAA": "E",
                   "UAG": "Stop",
                   "CAG": "Q",
                   "AAG": "K",
                   "GAG": "E",
                   "UGU": "C",
                   "CGU": "R",
                   "AGU": "S",
                   "GGU": "G",
                   "UGC": "C",
                   "CGC": "R",
                   "AGC": "S",
                   "GGC": "G",
                   "UGA": "Stop",
                   "CGA": "R",
                   "AGA": "R",
                   "GGA": "G",
                   "UGG": "W",
                   "CGG": "R",
                   "AGG": "R",
                   "GGG": "G"
                   }

unique_aa = set(rna_codon_table.values())

reverse_rna_codon_table = dict.fromkeys(unique_aa, 0)

for v in rna_codon_table.values():
    reverse_rna_codon_table[v] += 1

print(reverse_rna_codon_table)

protein_string = input().strip()

tn = 1

for aa in protein_string:
    tn *= reverse_rna_codon_table[aa]
    tn %= 1000000

tn *= 3
tn %= 1000000
print(tn)
