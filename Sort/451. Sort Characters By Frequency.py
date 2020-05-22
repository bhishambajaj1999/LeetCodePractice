class Solution:
    def frequencySort(self, s: str) -> str:
        x = Counter(s)
        t=[]
        x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse = 1)}
        for i in x:
            for j in range(x[i]):
                t.append(i)
        return "".join(t)


