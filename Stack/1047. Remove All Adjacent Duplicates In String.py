class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk=[""]
        for c in S:
            if stk[-1]==c:
                stk.pop(-1)
            else:
                stk.append(c)
                        
        return "".join(stk)
