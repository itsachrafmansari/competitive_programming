ab = []
for c in range(int(input())):
    ab.append(input())
for d in ab:
    x = 0
    for y in (int(i) for i in d.split()):
        x += y
    print(x)
