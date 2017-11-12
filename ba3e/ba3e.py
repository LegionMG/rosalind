with open('dataset.txt', 'r') as f:
    t = f.read().split('\n')

k = len(t[0]) - 1
s = t[1]
d = dict()
for kmer in t:
    z = kmer[:-1]
    print(z)
    if z not in d.keys():
        d[z] = []
    d[z].append(kmer[1:])


print(d)

with open('ans.txt', 'w') as f:
    for key in d.keys():
        f.write('{0} -> {1}'.format(key, ','.join(d[key])))
        f.write('\n')