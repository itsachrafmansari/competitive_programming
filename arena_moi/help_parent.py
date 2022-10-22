lns = []
for N in range(int(input())):
    lns.append(input().split())
i = 1
for al in lns:
    x = [y for y in al[1]]
    x.pop(int(al[0]) - 1)
    print(i, ''.join(y for y in x))
    i += 1
