class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = 0

        for num in range(n+1):
            if num % m == 0:
                s -= num
            else:
                s += num

        return s
