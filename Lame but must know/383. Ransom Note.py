class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        for i in r:
            if i not in m or r[i] > m[i]:
                return False
        return True
