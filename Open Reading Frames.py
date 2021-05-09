from rosalind_functions import dna_to_rna, reverse_complement, read_fasta, RNA_CODON_TABLE


def get_orf_seq(hyp_prot_slice: list):
    orf_seq = ""
    for aa in hyp_prot_slice:
        if aa != "Stop":
            orf_seq += aa
        elif aa == "Stop":
            return (orf_seq)
        else:
            return (None)


def find_orf(hyp_prot: list):
    ORFs_local = set()
    for i, aa in enumerate(hyp_prot):
        if aa == "M":
            orf = get_orf_seq(hyp_prot[i:])
            if orf is not None:
                ORFs_local.add(orf)

    return (ORFs_local)


def shift_rna_and_to_hyp_prot(rna: str, shift: int):
    rna = rna[shift:]
    codons = [rna[i:i + 3] for i in range(0, len(rna), 3)]
    hyp_prot = [RNA_CODON_TABLE[x] for x in codons if len(x) == 3]
    return (hyp_prot)


dna = read_fasta("multifasta.fasta")["Rosalind_0238"]
rna = dna_to_rna(dna)
rev_rna = dna_to_rna(reverse_complement(dna))

ORFs_total = set()

# Without shift
tmp1 = shift_rna_and_to_hyp_prot(rna, 0)
tmp2 = shift_rna_and_to_hyp_prot(rna, 1)
tmp3 = shift_rna_and_to_hyp_prot(rna, 2)
ORFs_total |= (find_orf(shift_rna_and_to_hyp_prot(rna, 0)))
ORFs_total |= (find_orf(shift_rna_and_to_hyp_prot(rna, 1)))
ORFs_total |= (find_orf(shift_rna_and_to_hyp_prot(rna, 2)))

# Shifted
tmp4 = shift_rna_and_to_hyp_prot(rev_rna, 0)
tmp5 = shift_rna_and_to_hyp_prot(rev_rna, 1)
tmp6 = shift_rna_and_to_hyp_prot(rev_rna, 2)
ORFs_total |= (find_orf(shift_rna_and_to_hyp_prot(rev_rna, 0)))
ORFs_total |= (find_orf(shift_rna_and_to_hyp_prot(rev_rna, 1)))
ORFs_total |= (find_orf(shift_rna_and_to_hyp_prot(rev_rna, 2)))

print("\n".join(ORFs_total))
