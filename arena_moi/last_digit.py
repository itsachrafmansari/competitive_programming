def fac(x):
    if x == 0:
        return 1
    else:
        return x * fac(x - 1)


lns = []
for N in range(int(input())):
    lns.append(int(input()))

for al in lns:
    if al >= 5:
        print(0)
    else:
        print(str(fac(al))[-1:])
