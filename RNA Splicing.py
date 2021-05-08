from rosalind_functions import rna_to_prot, find_motif, dna_to_rna

gene = ""

with open("multifasta.fasta", "r") as inp:
    gene_flag = 0
    intron = ""
    next(inp)
    for line in inp:
        if not line.startswith(">") and gene_flag == 0:
            gene += line.strip()
        else:
            gene_flag = 1
            if not line.startswith(">"):
                intron += line.strip()
            if intron != "":
                intron_start = find_motif(gene, intron)[0]
                a = gene[:intron_start]
                b = gene[intron_start + len(intron):]
                gene = gene[:intron_start] + gene[intron_start + len(intron):]
                intron = ""
                continue
    print(gene)
    print(dna_to_rna(gene))
    protein = rna_to_prot(dna_to_rna(gene))

print(protein)
