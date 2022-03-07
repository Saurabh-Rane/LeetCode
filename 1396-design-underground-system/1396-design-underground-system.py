class UndergroundSystem:

    def __init__(self):
        # customerid: (timestart, startstation)
        self.i = collections.defaultdict(tuple)
        # (startstation, endstation): [timeend - timestart]
        self.o = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.i[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starttime, startstation = self.i[id]
        totaltime = t - starttime
        self.o[(startstation, stationName)].append(totaltime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.o[(startStation, endStation)]) / len(self.o[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)