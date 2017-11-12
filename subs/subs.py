with open('dataset.txt', 'r') as f:
	t = f.read()

haystack, needle = t.split('\n')
from regex import finditer
print(' '.join([str(match.span()[0]+1) for match in finditer(needle, haystack, overlapped=True)]))
