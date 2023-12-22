class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        output = []

        for i in range(len(candies)):
            output.append(True if candies[i] + extraCandies >= maxCandies else False)

        return output
