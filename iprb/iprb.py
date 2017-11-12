k, m, n = map(int, input().split())

s = k + m + n

o_d = (k / s * (k - 1) / (s - 1))

d_r = 2 * (k / s * n / (s - 1))

d_h = 2 * (k / s * m / (s - 1))

h_h = 3/4 * (m / s * (m - 1) / (s - 1))

h_r = (m / s * n / (s - 1))


print(o_d, d_r, d_h, h_h, h_r)

print(o_d + d_r + d_h + h_h + h_r)


