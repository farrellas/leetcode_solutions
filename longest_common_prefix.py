class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        for s in strs:
            curr = ""
            for i in range(len(s)):
                if not output:
                    break
                if i < len(output) and s[i] == output[i]:
                    curr += s[i]
                else:
                    break
            output = curr
        return output