s1 = input().strip()
s2 = input().strip()


d = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        d += 1

print(d)