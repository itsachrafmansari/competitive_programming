from math import inf


class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        firstMax, secondMax, secondMin, firstMin = -inf, -inf, inf, inf

        for num in nums:
            if num > firstMax:
                secondMax = firstMax
                firstMax = num
            elif num > secondMax:
                secondMax = num
            
            if num < firstMin:
                secondMin = firstMin
                firstMin = num
            elif num < secondMin:
                secondMin = num

        return (firstMax * secondMax) - (secondMin * firstMin)
