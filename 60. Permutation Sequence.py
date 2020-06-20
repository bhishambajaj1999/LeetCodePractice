class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]
        k -= 1
        per = ''
        
        while n > 0:
            n -= 1
            i,k = divmod(k,math.factorial(n))
            #print(n,i,k,nums[i])
            per += str(nums[i])
            nums.remove(nums[i])
            
        
        return per
    

