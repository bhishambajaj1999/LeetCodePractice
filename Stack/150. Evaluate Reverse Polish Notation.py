class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        op = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in op:
                s.append(i)
            else:
                m = int(s.pop()) 
                n = int(s.pop())
                if i == "+":
                    s.append(m+n)
                if i == "-":
                    s.append(n-m)
                if i == "*":
                    s.append(m*n)
                if i == "/":
                    s.append(int(n/m))
        return s[-1]
