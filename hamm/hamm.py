with open('dataset.txt', 'r') as f:
	t = f.read()

a, b = t.split('\n')

print(sum([1 if a[i] != b[i] else 0 for i in range(len(a))]))
