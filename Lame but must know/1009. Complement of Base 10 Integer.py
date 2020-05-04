class Solution:
    def findComplement(self, num: int) -> int:
        n = bin(num).replace("0b","")
        t = ""
        for i in n:
            if i == "1":
                t += "0"
            else:
                t += "1"
        return int(t,2)
        
"""

Math Approach :

X = 1
while N > X: X = X*2 + 1
return X-N

"""
