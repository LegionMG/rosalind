with open('dataset.txt', 'r') as f:
    t = f.read()

fasta = t.split()

dna = ''.join(fasta[1:])

ans = []

def is_complement(d1, d2):
    d = {"T": "A", "C": "G", "G":"C", "A":"T"}
    for i in range(len(d1)):
        if d[d1[i]] == d2[i]:
            continue
        else:
            return False

    print(d1, d2)
    return True

for l in range(4, 13):
    for i in range(0, len(dna)-l+1):
        if is_complement(dna[i:i+l], dna[i:i+l][::-1]):
            ans.append("{0} {1}".format(i+1, l))


print('\n'.join(ans))
with open('ans.txt', 'w') as f:
    f.write('\n'.join(ans))