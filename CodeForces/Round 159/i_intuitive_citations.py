numberOfNames = int(input())
surnames = []

for _ in range(numberOfNames):
    fullName = input()
    surname = fullName.split()[1]
    surnames.append(surname)

surnames.sort()

print(f"{surnames[0]} et al.")
