with open('dataset.txt', 'r') as f:
    t = f.read().split('\n')

k = int(t[0]) - 1
s = t[1]
d = dict()
print(s)
for i in range(len(s)-k+1):
    z = s[i:i+k]
    if z not in d.keys():
        d[z] = []
    if i+k+1 <= len(s):
        d[z].append(s[i+1:i+k+1])


print(d)

with open('ans.txt', 'w') as f:
    for key in d.keys():
        f.write('{0} -> {1}'.format(key, ','.join(d[key])))
        f.write('\n')