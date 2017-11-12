with open('dataset.txt', 'r') as f:
	t = f.read()

patterns = t.split()

output_arr = []

output_arr += list(patterns[0])

for i in range(1, len(patterns)):
	output_arr.append(patterns[i][-1])

print(''.join(output_arr))
with open('ans.txt', 'w') as f:
	f.write(''.join(output_arr))