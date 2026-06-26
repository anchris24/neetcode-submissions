class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target:
            return 0

        left, currsum = 0, 0
        minlength = len(nums)

        for right in range(len(nums)):
            currsum += nums[right]

            while currsum >= target:
                minlength = min(minlength, right - left + 1)
                currsum -= nums[left]
                left += 1
        
        return minlength

            