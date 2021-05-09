RNA_CODON_TABLE = {"UUU": "F",
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
                   "AUG": "M",  # Start codon
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
DNA_COMPLEMENT_TABLE = {"A": "T",
                        "C": "G",
                        "G": "C",
                        "T": "A"}
RNA_COMPLEMENT_TALBE = {"A": "U",
                        "C": "G",
                        "G": "C",
                        "T": "A"}


def reverse_complement(dna: str):
    rev_compl = ""
    dna = dna.upper()
    for nuc in reversed(dna):
        rev_compl += DNA_COMPLEMENT_TABLE[nuc]
    return (rev_compl)


def dna_to_rna(dna):
    rna = dna.replace("T", "U")
    return (rna)


def rna_to_prot(rna: str):
    aa = ""
    codon = ""
    start = False
    for nuc in rna:
        if len(codon) < 2:
            codon += nuc
        else:
            if len(codon) == 2:
                codon += nuc
            if RNA_CODON_TABLE[codon] == "Stop":
                return (aa)
            if start == True:
                aa += RNA_CODON_TABLE[codon]
            if codon == "AUG" and start == False:
                aa += RNA_CODON_TABLE[codon]
                start = True
            codon = ""
    return (aa)


def read_fasta(file):
    dna_strings = {}
    gene = ""
    with open(file, "r") as fasta:
        for line in fasta:
            if line.startswith(">"):
                if gene != "":
                    dna_strings[id] = gene
                id = line.strip()[1:]
                gene = ""
            if not line.startswith(">"):
                gene += line.strip()
        dna_strings[id] = gene
    return (dna_strings)


def find_motif(dna: str, motif: str):
    locs = []
    ml = len(motif)
    for i in range(len(dna)):
        if dna[i] == motif[0]:
            if i + ml < len(dna) and dna[i: i + ml] == motif:
                locs.append(i)
    return (locs)


if __name__ == "__main__":
    print("it's library with some useful functions")
