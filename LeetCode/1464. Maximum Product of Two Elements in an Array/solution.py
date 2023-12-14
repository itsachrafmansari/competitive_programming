class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstMax = {"value": -inf, "index": None}
        secondMax = {"value": -inf, "index": None}

        for i, num in enumerate(nums):
            if num > firstMax["value"]:
                secondMax["value"] = firstMax["value"]
                secondMax["index"] = firstMax["index"]
                firstMax["value"] = num
                firstMax["index"] = i
            elif num > secondMax["value"]:
                secondMax["value"] = num
                secondMax["index"] = i

            # Debug ------------------------
            # print(num, firstMax, secondMax)

        return (firstMax["value"] - 1) * (secondMax["value"] - 1)
