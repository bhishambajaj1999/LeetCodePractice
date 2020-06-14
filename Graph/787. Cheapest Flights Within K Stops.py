class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        cost = [float('inf')] * n
        cost[src] = 0
        
        for _ in range(K+1):
            c = cost[:]
            for s,d,w in flights:
                c[d] = min(c[d], cost[s] + w)
            cost = c
        
        return -1 if cost[dst] == float('inf') else cost[dst]
