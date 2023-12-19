class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] * nums[1]) - (nums[-2] * nums[-1])
