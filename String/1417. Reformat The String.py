class Solution:
    def reformat(self, s: str) -> str:
        c = [i for i in s if i.isalpha()]
        d = [i for i in s if i.isdigit()]
        if abs(len(c) - len(d)) > 1:
            return ""
        k = ""
        if len(c) < len(d):
            c,d = d,c
        for i in range(len(c)+len(d)):
            if(i%2 == 0):
                k += c[i//2]
            else:
                k += d[i//2]
        return k
