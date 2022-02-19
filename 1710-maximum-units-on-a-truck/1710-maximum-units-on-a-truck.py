class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True, key = lambda x: x[1])
        res = 0
        for no, unit in boxTypes:
            if no < truckSize:
                res += unit * no
                truckSize -= no
            else:
                res += truckSize * unit
                break
        return res