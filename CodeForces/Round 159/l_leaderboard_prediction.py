nLines, hours = list(map(int, input().split()))

problemsMinutes = []
for _ in range(nLines):
    minutes = int(input())
    problemsMinutes.append(minutes)
problemsMinutes.sort()


problemsSolved = 0
totalMinutes = hours * 60
timePenalty = 0
timePassed = 0

for problemTime in problemsMinutes:
    # print(problemTime, timePenalty, timePassed)

    if timePassed + problemTime <= totalMinutes:

        timePassed += problemTime
        problemsSolved += 1
        timePenalty += timePassed

print(problemsSolved, timePenalty)
