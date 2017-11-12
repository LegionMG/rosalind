def overlap(str1, str2):
    s1last = len(str1) - 1
    s2len = len(str2)
    overlap_p, overlap_l = 0, 0
    for i in range(s2len):
        if is_overlap(i, str1, str2): overlap_p = i
    return overlap_p

def merge(str1, str2, pos):
    return str1 + str2[pos:]


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

q = list(ss.values())
hl = len(q[0])//2



print(q)
i = 0
flag = True
while len(q) > 1 or not flag:
    if i < 3: print(q)
    i+=1
    if flag: one, two = q.pop(0), q.pop(0)
    flag = True
    o1 = overlap(one, two)
    o2 = overlap(two, one)
    if o1 > hl+1:
        s = merge(one, two, o1)
        q.append(s)
    elif o2 > hl+1:
        s = merge(two, one, o2)
        q.append(s)
    else:
        q.append(two)
        two = q.pop(0)
        flag = False


print(q)

with open('ans.txt', 'w') as f:
	f.write(''.join(q))