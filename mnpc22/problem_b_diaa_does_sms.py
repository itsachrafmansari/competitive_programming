n  = int(input())
info = {}
info1 = {}
klist = []
for i in range(n):
    misdn, imsi = input().split(",")
    info[misdn] = imsi
p = int(input())
for j in range(p):
    region, misdn1 = input().split(",")
    info1[misdn1] = region
    try:
        klist.append(f"{misdn1},{info[misdn1]},{info1[misdn1]}")
    except:
        klist = klist
klist.sort()
print("\n".join(klist))
