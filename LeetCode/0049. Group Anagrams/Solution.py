class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            sortedStr = ''.join(sorted(string))

            if sortedStr in groups:
                groups[sortedStr].append(string)
            else:
                groups[sortedStr] = [string]

        return [group for group in groups.values()]
