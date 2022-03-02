class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for index, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                i, j = stack.pop()
                res[i] = index - i
            stack.append((index, val))
            
        return res
        