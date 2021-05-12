import re

from rosalind_functions import find_motif
from Bio import SeqIO
from io import StringIO  # SeqIO.parse работает только с чтением файла
import requests


def download_data(uniprot_ids: list) -> dict:
    uniprot_seqs = {}
    base_url = "http://www.uniprot.org/uniprot/"
    for id in uniprot_ids:
        url = base_url + id + ".fasta"
        response = requests.post(url)
        data = StringIO(''.join(response.text))
        seqio_tmp = SeqIO.parse(data, "fasta")
        for record in seqio_tmp:
            uniprot_seqs[id] = str(record.seq)

    return (uniprot_seqs)


def check_for_motif(uniprot_seqs: dict, motif: str):
    motif_re = "N(?:(?![PBJOUXZ])[A-Z]){1}[ST]{1}(?:(?![PBJOUXZ])[A-Z]){1}"
    for id, seq in uniprot_seqs.items():
        motif_locs = find_motif(seq, motif_re, True)
        if len(motif_locs) != 0:
            print(id)
            for searched_motif in motif_locs:
                print(searched_motif + 1, end=" ")
            print("\n", end = "")

if __name__ == "__main__":
    lines = [line.rstrip('\n') for line in open("file.txt")]

    ids_list = download_data(lines)
    check_for_motif(ids_list, "")
