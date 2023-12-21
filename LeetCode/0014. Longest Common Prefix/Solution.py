class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) <= 1:
            return strs[0]

        maxL = ""
        for x in zip(*strs):

            if len(set(x)) > 1:
                break

            maxL += x[0]

        return maxL
