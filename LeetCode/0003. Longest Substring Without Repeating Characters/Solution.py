class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = 0
        i, j = 0, 0

        while i <= j < len(s):
            chars = {}
            foundDuplicates = False

            for char in s[i:j+1]:
                if char in chars:
                    i += 1
                    foundDuplicates = True
                    break
                else:
                    chars[char] = 0

            if not foundDuplicates:
                maxLength = max(maxLength, j-i+1)
                j += 1

        return maxLength
