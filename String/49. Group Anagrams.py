class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p = collections.defaultdict(list)
        for s in strs:
            p[tuple(sorted(s))].append(s)
        return p.values()
    
        
