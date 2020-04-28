class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.d = Counter(self.nums)
        
    def showFirstUnique(self) -> int:
        for i in self.d:
            if self.d[i] == 1:
                return i
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        if value in self.d:
            self.d[value] += 1
        else:
            self.d[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
