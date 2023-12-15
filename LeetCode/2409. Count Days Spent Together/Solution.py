class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arriveAliceDays, leaveAliceDays = self.dateToDays(arriveAlice, leaveAlice)
        arriveBobDays, leaveBobDays = self.dateToDays(arriveBob, leaveBob)

        if (leaveAliceDays < arriveBobDays) or (leaveBobDays < arriveAliceDays):
            return 0
        else:
            return min(leaveAliceDays, leaveBobDays) - max(arriveAliceDays, arriveBobDays) + 1

    def dateToDays(self, arriveDate: str, leaveDate: str) -> tuple[int, int]:
        daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        arriveDays = sum(daysPerMonth[:int(arriveDate[:2]) - 1], int(arriveDate[3:]))
        leaveDays = sum(daysPerMonth[:int(leaveDate[:2]) - 1], int(leaveDate[3:]))

        return arriveDays, leaveDays
