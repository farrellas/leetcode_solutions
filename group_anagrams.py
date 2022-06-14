class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        for string in strs:
            chars = [0] * 26
            for char in string:
                chars[ord(char) - ord('a')] += 1
            output[tuple(chars)].append(string)
        return output.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        for string in strs:
            key = tuple(sorted(string))
            output[key].append(string)
        return output.values()