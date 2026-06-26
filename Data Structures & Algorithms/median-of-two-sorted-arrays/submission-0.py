class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        medid = (len(nums1) + len(nums2) + 1) // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1)
        if not nums1:
            return nums2[len(nums2) // 2] if len(nums2)%2 == 1 else (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2

        while True:
            i = (left + right) // 2
            j = medid - i

            Aleft = nums1[i-1] if i > 0 else float('-inf')
            Aright = nums1[i] if i < len(nums1) else float('inf')
            Bleft = nums2[j-1] if j > 0 else float('-inf')
            Bright = nums2[j] if j < len(nums2) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                break
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1

        
        if (len(nums1) + len(nums2)) % 2 == 1:
            return max(Aleft, Bleft)
        else:
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
