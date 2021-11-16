from collections import Counter

inp = [c for c in str(input())]

d = Counter(inp)['1'] - Counter(inp)['0']

print(abs(d))
