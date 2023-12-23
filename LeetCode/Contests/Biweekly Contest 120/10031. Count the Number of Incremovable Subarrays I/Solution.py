class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return 1

        subArrays = 0

        for windowSize in range(1, len(nums) + 1):
            for startingIndex in range(0, len(nums) + 1 - windowSize):
                newArray = []
                for k in range(len(nums)):

                    if not startingIndex <= k < startingIndex + windowSize:
                        newArray.append(nums[k])

                # print(nums, nums[startingIndex: startingIndex + windowSize], newArray, self.isIncremental(newArray))
                if self.isIncremental(newArray):
                    subArrays += 1

        return subArrays

    def isIncremental(self, nums: list[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i] >= nums[i + 1]:
                return False

        return True
