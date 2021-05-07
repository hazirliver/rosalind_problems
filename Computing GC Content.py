gene = ""
gc_dict = {}

def gc_foo(gene: str):
    gc = 0
    for s in gene:
        if s == "G" or s == "C":
            gc += 1
    return (gc / len(gene))


with open("gc.txt", "r") as fasta:
    for line in fasta:
        if line.startswith(">"):
            if gene != "":
                gc_dict[id] = gc_foo(gene)
            id = line.strip()[1:]
            gene = ""
        if not line.startswith(">"):
            gene += line.strip()
    gc_dict[id] = gc_foo(gene)

gc_max_id = max(gc_dict, key=gc_dict.get)
print(gc_dict)
print(gc_max_id)
print(gc_dict[gc_max_id] * 100)
