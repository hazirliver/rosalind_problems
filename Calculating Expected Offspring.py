import numpy as np

dom_prob = np.array([1, 1, 1, 0.75, 0.5, 0])

genotypes = np.fromiter(map(int, input().split()), dtype=np.int)

print(np.dot(genotypes * 2, dom_prob))
