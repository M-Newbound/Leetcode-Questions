class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        state = {}
        order = []

        def dfs(course):
            if course in state:
                return state[course] == 1
            state[course] = 0
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            state[course] = 1
            order.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return order
