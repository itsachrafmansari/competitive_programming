line1 = input().split()
x, A, B = int(line1[0]), int(line1[1]), int(line1[2])
line2 = [i for i in input()]

c = 0
for j in line2:
    for k in line2:
        num = int(j + k)
        if A <= num <= B and num % x == 0:
            c += 1

print(c)
