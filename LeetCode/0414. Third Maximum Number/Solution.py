class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax = secondMax = thirdMax = float("-inf")

        for num in nums:
            if num > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = num
            elif firstMax > num > secondMax:
                thirdMax = secondMax
                secondMax = num
            elif secondMax > num > thirdMax:
                thirdMax = num

        return firstMax if thirdMax == float("-inf") else thirdMax
