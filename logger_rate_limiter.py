class Logger:

    def __init__(self):
        self.log = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.log.get(message, float('-inf')) + 10 <= timestamp:
            self.log[message] = timestamp
            return True
        return False

# slightly faster due to not needing to do aritmetic operation every time

class Logger:

    def __init__(self):
        self.log = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.log.get(message, 0):
            return False
        self.log[message] = timestamp + 10
        return True