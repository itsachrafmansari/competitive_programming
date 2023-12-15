class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxOnesRowIndex = 0
        maxOnes = 0

        for i, row in enumerate(mat):
            currentOnes = row.count(1)

            if currentOnes > maxOnes:
                maxOnes = currentOnes
                maxOnesRowIndex = i

        return [maxOnesRowIndex, maxOnes]
