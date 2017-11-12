with open('dataset.txt', 'r') as f:
	t = f.read()

d = {'A': 'T', 'C':'G', 'G':'C', 'T':'A'}

with open('res.txt', 'w') as f:
	f.write(''.join([d[x] for x in t.replace('\n', '')[::-1]]))

