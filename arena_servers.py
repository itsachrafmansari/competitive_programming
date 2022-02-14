tests = int(input())

for i in range(tests):
    l1 = input().split()
    l2 = input().split()

    N, c = int(l1[0]), int(l1[1])
    clusters = [int(clus) for clus in l2]
    servers = 0

    for cluster in clusters:
        rest = cluster % c
        if not rest:
            servers += cluster // c
        else:
            servers += (cluster // c) + 1

    print(servers)
