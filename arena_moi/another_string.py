number_of_cases = int(input())

for case in range(number_of_cases):
    str2list = list(input())
    str2list.reverse()
    print("".join(str2list))
