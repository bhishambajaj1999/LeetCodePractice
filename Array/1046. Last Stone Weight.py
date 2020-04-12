class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while(len(stones) > 1):
            f = stones.pop(-1)
            s = stones.pop(-1)
            bisect.insort(stones,abs(f-s))
            print(stones)
        return stones[0]
