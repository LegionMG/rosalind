with open('dataset.txt', 'r') as f:
	t = f.read()
with open('rna.txt', 'w') as f:
	f.write(t.replace('T', 'U'))

