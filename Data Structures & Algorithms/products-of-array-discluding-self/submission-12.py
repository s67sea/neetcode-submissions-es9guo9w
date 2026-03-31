class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        forwards = [1]*n #product of 1...i
        backwards = [1]*n #product of i...end
        products = [1]*n

        for i in range(1,n):
            forwards[i] = forwards[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            backwards[i] = backwards[i+1]*nums[i+1]
        

        for i in range(n):
            products[i] = forwards[i] * backwards[i]
        
        return products

