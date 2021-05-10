### Задача о поиске наибольшей общей подпоследовательности (LCS)
### Сначала учимся искать длину LCS в случае 2 последовательностей
### Потом определеим сами эти подпоследовательности
import numpy as np

from rosalind_functions import read_fasta


### Поиск наибольшей общей ПОДПОСЛЕДОВАТЕЛЬНОСТИ
def fill_lc_subsequence_mat(a, b):
    lc_subseqnce_mat = np.zeros((len(a) + 1, len(b) + 1))
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                lc_subseqnce_mat[i][j] = 1 + lc_subseqnce_mat[i - 1][j - 1]
            else:
                lc_subseqnce_mat[i][j] = max(lc_subseqnce_mat[i - 1][j], lc_subseqnce_mat[i][j - 1])
    return (lc_subseqnce_mat)


def get_lc_subsequence_seq(a, b):
    lc_subsequence_mat = fill_lc_subsequence_mat(a, b)

    lc_subsequence_seq = ""
    i = len(a)
    j = len(b)
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lc_subsequence_seq += a[i - 1]
            i -= 1
            j -= 1
        else:
            if lc_subsequence_mat[i][j - 1] >= lc_subsequence_mat[i - 1][j]:
                i = i
                j -= 1
            else:
                i -= 1
                j = j
    return (lc_subsequence_seq[::-1])


### Поиск наибольшей общей ПОДСТРОКИ

def fill_lc_substring_mat(a, b):
    lc_substring_mat = np.zeros((len(a) + 1, len(b) + 1))
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                lc_substring_mat[i][j] = 1 + lc_substring_mat[i - 1][j - 1]
            else:
                lc_substring_mat[i][j] = 0
    return (lc_substring_mat)


def get_lc_substring_seq(a, b):
    lc_substring_mat = fill_lc_substring_mat(a, b)

    lc_substring_seq = ""

    ind_max = np.unravel_index(np.argmax(lc_substring_mat, axis=None), lc_substring_mat.shape)
    i = ind_max[0]
    j = ind_max[1]

    while lc_substring_mat[i][j] > 0:
        lc_substring_seq += a[i - 1]
        i -= 1
        j -= 1

    return (lc_substring_seq[::-1])


### Поиск наибольшей общей ПОДСТРОКИ из N строк
def ngrams_dict(s):
    ngrams = [s[i: j] for i in range(len(s))
              for j in range(i + 2, len(s) + 1)]
    ngrams_dict = dict.fromkeys(ngrams, 0)
    return (ngrams_dict)


def long_substr(data: dict):
    ngrams_to_check = ngrams_dict(data[0])
    ls = ""
    ls_len = 0

    for ngram in ngrams_to_check:
        for seq in data[1:]:
            if ngram in seq:
                ngrams_to_check[ngram] += 1
                if ngrams_to_check[ngram] > ls_len:
                    ls_len = ngrams_to_check[ngram]
                    ls = ngram

    return (ls)


seqs_dict = read_fasta("multifasta.fasta")
seqs_combs = list(seqs_dict.values())

print(long_substr(seqs_combs))
