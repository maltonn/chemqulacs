from math import comb
from itertools import combinations
n_electron=3
excitation_number=10


for m in range(n_electron, 9999):
    if comb(m, n_electron) >= excitation_number + 1:
        break
occ_indices_lst = sorted(
    list(combinations(range(m), n_electron)),
    key=lambda lst: sum([2**a for a in lst]),
)[: excitation_number + 1]

print(occ_indices_lst)