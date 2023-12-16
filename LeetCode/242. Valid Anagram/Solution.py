class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        letters_counter = {}

        for s_char, t_char in zip(s, t):
            if s_char in letters_counter:
                letters_counter[s_char] += 1
            else:
                letters_counter[s_char] = 1

            if t_char in letters_counter:
                letters_counter[t_char] -= 1
            else:
                letters_counter[t_char] = -1

        for key in letters_counter:
            if letters_counter[key] != 0:
                return False

        return True
