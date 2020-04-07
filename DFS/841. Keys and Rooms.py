class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        stack = []
        visited[0] = 1
        stack.append(0)
        while stack:
            k = rooms[stack.pop()]
            for i in k:
                if visited[i] != 1:
                    visited[i] = 1
                    stack.append(i)
        
        #print(visited)
        
        return all(visited)
                
