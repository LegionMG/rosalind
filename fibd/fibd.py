n, k = map(int, input().split())
i, p = 1, 1

birth = [0]

for j in range(1, n - 1):
    if j >= k-1:
        i, p = p, i+p-birth[j-k+1]
        ded = birth[j-k]
    else:
        i, p = p, i+p
    birth.append(i)
    print(p)
print(birth)
print(i, p)

def rabbit_pairs(n, m):
    sequence = list()
    for i in range(n):
        if i < 2:
            # Normal Fibonacci initialization
            total = 1
            sequence.append(total)
        elif (i < m) or (m == 0):
            # Normal Fibonacci calculation
            total = sequence[i - 1] + sequence[i - 2]
            sequence.append(total)
        elif i == m:
            # Now we need R(n - (m + 1)), but i - (m + 1) < 0, so we have to
            # provide the missing value
            total = sequence[i - 1] + sequence[i - 2] - 1
            sequence.append(total)
        else:
            # i - (m + 1) >= 0, so we can get the value from the sequence
            total = sequence[i - 1] + sequence[i - 2] - sequence[i - (m + 1)]
            sequence.append(total)
    return total

print(rabbit_pairs(n, k))