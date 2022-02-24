class CustomStack:

    def __init__(self, maxSize: int):
        self.customStack = [0] * maxSize
        self.maxSize = maxSize
        self.currsize = 0
        
    def push(self, x: int) -> None:
        if self.currsize < self.maxSize:
            self.customStack[self.currsize] = x
            self.currsize += 1
            print(self.customStack, self.currsize, self.maxSize)
        
    def pop(self) -> int:
        if self.currsize:
            self.currsize -= 1
            return self.customStack[self.currsize]
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < self.currsize:
                self.customStack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)