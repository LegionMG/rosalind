import re

with open('dataset.txt', 'r') as f:
	t = f.read()

codons = re.findall('..?.?', t)

d = {}
with open('codon.txt', 'r') as f:
	t = f.read()

for line in t.split('\n'):
	l = line.split()
	for codon in l[1:]:
		d[codon] = l[0]

print(d)
with open('ans.txt', 'w') as f:
	f.write(''.join([d[x] for x in codons if d[x]!='STOP']))

