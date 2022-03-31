class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursemap = {i:[] for i in range(numCourses)}
        
        for i, pre in prerequisites:
            coursemap[i].append(pre)
            
        visitset = set()
        
        def dfs(course):
            if course in visitset:
                return False
            if coursemap[course] == []:
                return True
            
            visitset.add(course)
            for i in coursemap[course]:
                if not dfs(i):
                    return False
            visitset.remove(course)
            coursemap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        