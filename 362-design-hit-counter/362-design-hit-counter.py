class HitCounter:

    def __init__(self):
        self.time = [0] * 300
        self.count = [0] * 300

    def hit(self, timestamp: int) -> None:
        index = timestamp % 300
        if self.time[index] != timestamp:
            self.time[index] = timestamp
            self.count[index] = 1
        else:
            self.count[index] += 1

    def getHits(self, timestamp: int) -> int:
        res = 0
        for i in range(300):
            if self.time[i] > timestamp - 300:
                res += self.count[i]
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)