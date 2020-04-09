class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s,t = [],[]
        for i in S:
            if i == "#": 
                if s:
                    s.pop() 
                else:
                    continue
            else:
                s.append(i)
        for i in T:
            if i == "#": 
                if t:
                    t.pop() 
                else:
                    continue
            else:
                t.append(i)
        return s == t
