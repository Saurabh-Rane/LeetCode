class OrderedStream:

    def __init__(self, n: int):
        self.buffer = [None] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.buffer[idKey - 1] = value
        stream = []
        
        while self.pointer < len(self.buffer) and self.buffer[self.pointer] != None:
            stream.append(self.buffer[self.pointer])
            self.pointer += 1
        
        return stream


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)