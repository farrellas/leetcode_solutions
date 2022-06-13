class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False
        
        stack = []
        opn = {'(', '[', '{'}
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in opn:
                stack.append(char)
            elif stack:
                if stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return len(stack) == 0


