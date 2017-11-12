with open('dataset.txt', 'r') as f:
	t = f.read()
print("{0} {1} {2} {3}".format(t.count('A'), t.count('C'), t.count('G'), t.count('T')))
