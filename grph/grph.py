def overlap(str1, str2):
    s1last = len(str1) - 1
    s2len = len(str2)
    overlap_p, overlap_l = 0, 0
    for i in range(s2len):
        suff = str1[i:]
        pref = str2[:(s2len - i)]
        if (suff == pref): overlap_p, overlap_l = i, len(suff)
    return overlap_p, overlap_l

def merge(str1, str2, pos):
    return str1[:pos] + str2

def is_overlap(num, str1, str2):
    return str1[-num:] == str2[:num] and str1 != str2


with open('dataset.txt', 'r') as f:
	t = f.read()

s = t.split('\n')

ss = dict()
i = 0
while i < len(s)-1:
    name = s[i][1:]
    dna = []
    i+=1
    while i < len(s):
        if s[i][0] == '>':
            break
        dna.append(s[i])
        i+=1
        if i == len(s):
            break
    ss[name] = ''.join(dna)

q = list(ss.keys())

print(ss)
print(q)
ans = []

for i in range(len(q)):
    for j in range(len(q)):
        if i == j:
            continue
        if is_overlap(3, ss[q[i]], ss[q[j]]):
            ans.append(q[i]+' '+ q[j])


# print(ans)
with open('ans.txt', 'w') as f:
	f.write('\n'.join(ans))