import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        noteCount = collections.Counter(ransomNote)
        magCount = collections.Counter(magazine)
            
        for letter in noteCount.keys():
            if noteCount[letter] > magCount.get(letter, 0):
                return False
        return True