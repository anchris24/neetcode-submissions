class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums))
        res[0] = nums[0]

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != 0:
                res[i] = post * res[i-1]
            else:
                res[i] = post
            post *= nums[i]
        return res