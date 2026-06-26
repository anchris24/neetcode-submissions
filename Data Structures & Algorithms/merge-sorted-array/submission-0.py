class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        id1, id2 = m-1, n-1
        pos = m + n - 1
        while id2 >= 0:
            a, b = nums1[id1], nums2[id2]
            if id1 < 0 or a < b:
                nums1[pos] = nums2[id2]
                id2 -= 1
            else:
                nums1[pos] = nums1[id1]
                id1 -= 1
            pos -= 1
        