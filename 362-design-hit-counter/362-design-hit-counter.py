class HitCounter:

    def __init__(self):
        self.index = [0] * 300
        self.count = [0] * 300

    def hit(self, timestamp: int) -> None:
        val = timestamp % 300
        if self.index[val] != timestamp:
            self.index[val] = timestamp
            self.count[val] = 1
        else:
            self.count[val] += 1
        

    def getHits(self, timestamp: int) -> int:
        res = 0
        for i in range(300):
            if timestamp >= self.index[i] > timestamp - 300:
                res += self.count[i]
        return res
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)