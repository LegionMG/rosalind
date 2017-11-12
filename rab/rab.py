n, k = map(int, input().split())
i, p = 1, 1
print(n, k)

for _ in range(1, n):
	i, p = p, k*i+p

print(i, p)
