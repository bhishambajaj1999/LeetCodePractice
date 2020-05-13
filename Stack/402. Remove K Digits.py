class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        out = []
        for i in num:
            while out and k and out[-1]>i:
                out.pop()
                k -= 1
            out.append(i)
        
        return ''.join(out[:-k or None]).lstrip('0') or '0'
