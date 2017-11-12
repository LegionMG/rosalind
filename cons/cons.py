with open('dataset.txt', 'r') as f:
	t = f.read()

z = t.split('>')
s = []
for line in z[1:]:
	l = line.split('\n')
	s.append(l[0])
	s.append(''.join(l[1:]))

d = {y: [0 for x in range(len(s[1]))] for y in 'AGTC'}
print(s)
for line in s:
	if line.startswith('R'):
		continue
	else:
		for i, l in enumerate(line):
			d[l][i] += 1

with open('ans.txt', 'w') as f:
	f.write(''.join(max(d.keys(), key=lambda k: d[k][i]) for i in range(len(s[1])))+'\n')
	for i in 'ACTG':
		f.write('{0}: {1}\n'.format(i, ' '.join(map(str, d[i]))))
