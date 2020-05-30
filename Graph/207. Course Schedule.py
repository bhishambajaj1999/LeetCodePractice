class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # Return True if finds a cycle
        def dfs(node, non_visited_set, visiting_set, visited_set):
            if node in visiting_set:
                return True
            if node in visited_set:
                return False
            
            transfer(node, non_visited_set, visiting_set)
            
            for neighbor in graph[node]:
                if dfs(neighbor, non_visited_set, visiting_set, visited_set):
                    return True
                
            transfer(node, visiting_set, visited_set)
            return False
            
        def transfer(node, source, destination):
            source.remove(node)
            destination.add(node)
        
        graph = [[] for x in range(numCourses)]
        for x, y in prerequisites:
            graph[y].append(x)
        non_visited_set = set()                
        visiting_set = set()
        visited_set = set()
        
        for index in range(numCourses):
            non_visited_set.add(index)
            
        for node in range(numCourses):            
            if dfs(node, non_visited_set, visiting_set, visited_set):
                return False
        return True
