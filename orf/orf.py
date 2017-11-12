import re

def rev_compl(st):
    s = st[::-1]
    d = {"T": "A", "C": "G", "G":"C", "A":"T"}
    return ''.join(d[x] for x in s)

with open('dataset.txt', 'r') as f:
    t = f.read()

fasta = t.split()
dna = ''.join(fasta[1:])

r_dna = rev_compl(dna)

starts = [m.start() for m in re.finditer('ATG', dna)]

starts_ = [m.start() for m in re.finditer('ATG', r_dna)]



d = {}
with open('codon.txt', 'r') as f:
    t = f.read()
ans = []

for line in t.split('\n'):
    l = line.split()
    for codon in l[1:]:
        d[codon] = l[0]

for start in starts:
    codons = re.findall('..?.?', dna[start:])
    an = []
    flag = False
    print(codons)
    for x in codons:
        #print(x, d[x])
        if len(x) != 3:
            break
        if d[x] != 'STOP':
            an.append(d[x])
        else:
            flag = True
            break
    if flag:
        a = ''.join(an)
        ans.append(a)

for start in starts_:
    codons = re.findall('..?.?', r_dna[start:])
    an = []
    flag = False
    print(codons)
    for x in codons:
        #print(x, d[x])
        if len(x) != 3:
            break
        if d[x] != 'STOP':
            an.append(d[x])
        else:
            flag = True
            break
    if flag:
        a = ''.join(an)
        ans.append(a)

ans = sorted(set(ans))
with open('ans.txt', 'w') as f:
    f.write('\n'.join(ans))

