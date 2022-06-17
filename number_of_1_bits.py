class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(format(n, "b"))
        return s.count('1')

class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for i in range(32):
            if (n & mask) != 0:
                bits += 1
            mask <<= 1
        return bits

