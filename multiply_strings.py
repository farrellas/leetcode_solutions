class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 += int(num1[i]) * (10 ** (len(num1) - 1 - i))
        for i in range(len(num2)):
            n2 += int(num2[i]) * (10 ** (len(num2) - 1 - i))
        print(n1, n2)
        return str(n1 * n2)

# not using int function
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 += (ord(num1[i]) - ord('0')) * (10 ** (len(num1) - 1 - i))
        for i in range(len(num2)):
            n2 += (ord(num2[i]) - ord('0')) * (10 ** (len(num2) - 1 - i))
        print(n1, n2)
        return str(n1 * n2)

# using hashmap
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        conv = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in range(len(num1)):
            n1 += conv[num1[i]] * (10 ** (len(num1) - 1 - i))
        for i in range(len(num2)):
            n2 += conv[num2[i]] * (10 ** (len(num2) - 1 - i))
        return str(n1 * n2)