class Solution:
    def simplifyPath(self, path: str) -> str:
        k = [t for t in path.split("/") if t]
        
        s = []
        
        for i in k:
            if(i==".."): s.pop() if s else None
            elif(i != "."): s += [i]
        
        return ("".join(["/","/".join(s)]))
