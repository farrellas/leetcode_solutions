class MyQueue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        output = self.q[0]
        if len(self.q) > 1:
            self.q = self.q[1:]
        else:
            self.q = []
        return output

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0