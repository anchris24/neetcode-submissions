class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = nums[0]

        for i in nums[1:]:
            currsum = max(i, currsum+i)
            maxsum = max(maxsum, currsum)
        # maxsum = max(maxsum, currsum)
        return maxsum