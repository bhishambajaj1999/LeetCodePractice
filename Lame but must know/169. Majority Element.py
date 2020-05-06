class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = Counter(nums)
        k = {t:v for t,v in sorted(k.items(), key = lambda i:i[1])}
        print(k)
        return k.popitem()[0]
        
