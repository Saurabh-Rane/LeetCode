class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        coursemap = {i:[] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            coursemap[course].append(pre)
            
        visitvalid, cycle = set(), set()
        output = []
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visitvalid:
                return True
            
            cycle.add(course)
            for pre in coursemap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visitvalid.add(course)
            output.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return output
        
        
        