class Solution:
    def intToRoman(self, num: int) -> str:
        romanList = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10],
                     ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400],
                    ['D', 500], ['CM', 900], ['M', 1000]]
        res = ''
        for sym, i in romanList[-1::-1]:
            if num // i:
                count = num // i
                res += sym * count
                num = num % i
        return res
        