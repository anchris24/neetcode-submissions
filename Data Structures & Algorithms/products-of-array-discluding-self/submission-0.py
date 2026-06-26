class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * (2+len(nums)), [1] * (2+len(nums))
        prefix[1] = nums[0]
        suffix[-2] = nums[-1]
        
        for i in range(2, len(prefix)-1):
            prefix[i] = prefix[i-1]*nums[i-1]
            suffix[-i-1] = suffix[-i]*nums[-i]

        ans = []
        for i in range(1, len(prefix)-1):
            ans.append(prefix[i-1] * suffix[i+1])
        return ans