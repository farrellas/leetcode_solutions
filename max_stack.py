class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        print(self.stack)
        return self.stack[-1]

    def peekMax(self):
        return max(self.stack)

    def popMax(self):
        maximum = self.peekMax()
        max_index = -1
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] == maximum:
                max_index = i
                break
        return self.stack.pop(max_index)