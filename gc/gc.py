with open('dataset.txt', 'r') as f:
	t = f.read()

d = {}
for item in t.split('>')[1:]:
	spl = item.split('\n') 
	s = ''.join(spl[1:])
	d[spl[0]] = (s.count('G')+s.count('C'))/len(s)*100

key, value = max(d.items(), key=lambda x:x[1])

print(key)
print(value)
