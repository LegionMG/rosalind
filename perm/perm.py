n = int(input())

arr = list(map(str,range(1, n+1)))

def shuffles_and_sum(arr, head=[]):
    if not len(arr):
        yield (head)
    else:
        for element in arr:
            yield from shuffles_and_sum([x for x in arr if x!= element], head+[element])


with open('ans.txt', 'w') as f:
    ans = list(shuffles_and_sum(arr))
    f.write(str(len(ans)))
    f.write('\n')
    for x in ans:
        f.write(' '.join(x))
        f.write('\n')