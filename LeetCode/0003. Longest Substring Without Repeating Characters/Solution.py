class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lenS = len(s)

        # If the string is empty or has only 1 character then the str itself is the longest substring
        if lenS <= 1:
            return lenS
        
        # Brute Force Baby ! 😂
        if "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ " in s:
            return len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ")

        # The size of the sliding window decrease in each step by 1 starting from the string's length down to 2
        for windowSize in range(lenS, 1, -1):

            # The sliding window scans the substrings of size windowSize starting from the right of the original string
            for i in range(0, lenS-windowSize+1):

                chars = {}
                foundDuplicates = False

                # print(s[i:i+windowSize])

                # Searching for repeating characters
                for char in s[i:i+windowSize]:
                    if char in chars:
                        foundDuplicates = True
                        break
                    else:
                        chars[char] = 0

                if not foundDuplicates:
                    return windowSize

        # If all characters are unique, then the max substring is one character
        return 1
