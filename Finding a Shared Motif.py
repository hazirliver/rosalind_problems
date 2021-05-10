### Задача о поиске наибольшей общей подпоследовательности (LCS)
### Сначала учимся искать длину LCS в случае 2 последовательностей
### Потом определеим сами эти подпоследовательности
import numpy as np
from rosalind_functions import read_fasta
from itertools import combinations


def fill_lcs_mat(a, b):
    lcs_mat = np.zeros((len(a) + 1, len(b) + 1))
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                lcs_mat[i][j] = 1 + lcs_mat[i - 1][j - 1]
            else:
                lcs_mat[i][j] = max(lcs_mat[i - 1][j], lcs_mat[i][j - 1])
    return (lcs_mat)


def get_lcs_seq(a, b):
    lcs_mat = fill_lcs_mat(a, b)

    lcs_seq = ""
    i = len(a)
    j = len(b)
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs_seq += a[i - 1]
            i -= 1
            j -= 1
        else:
            if lcs_mat[i][j - 1] >= lcs_mat[i - 1][j]:
                i = i
                j -= 1
            else:
                i -= 1
                j = j
    return (lcs_seq[::-1])


def get_lcs_seq_from_dict(seqs_dict, keys):
    key1 = keys[0]
    key2 = keys[1]
    return (get_lcs_seq(seqs_dict[key1], seqs_dict[key2]))


# seqs_dict = read_fasta("multifasta.fasta")
# print(seqs_dict)
# seqs_combs = list(combinations(seqs_dict.keys(), 2))
# print(seqs_combs)

# tmp = []

# for comb in seqs_combs:
#     tmp.append(get_lcs_seq_from_dict(seqs_dict, comb))

# tmp = map(get_lcs_seq_from_dict, seqs_dict, list(seqs_combs))
# print(tmp)
# print(list(tmp))




#
a, b = input().split()
lcs_mat = fill_lcs_mat(a, b)

print(lcs_mat)
print(get_lcs_seq(a, b))

# abcdede bedcadb
# bedcadb abcdede
# HABRAHABR HARBOUR
# HABRAHABR HARBOBR
