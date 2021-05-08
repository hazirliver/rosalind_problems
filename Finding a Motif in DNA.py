dna = input().strip()
motif = input().strip()

ml = len(motif)
locs = []
for i in range(len(dna)):
    if dna[i] == motif[0]:
        if dna[i: i + ml] == motif:
            locs.append(i + 1)

for _ in locs:
    print(_, end=" ")
