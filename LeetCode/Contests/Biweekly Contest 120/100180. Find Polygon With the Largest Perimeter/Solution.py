class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        nums = sorted(nums, reverse=True)

        left = 0
        right = len(nums)

        while left + 2 < right:

            if nums[left] >= sum(nums[left + 1: right]):
                left += 1
            else:
                return sum(nums[left: right])

        return -1
