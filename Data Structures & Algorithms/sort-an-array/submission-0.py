class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            
            left = mergesort(arr[:len(arr) // 2])
            right = mergesort(arr[len(arr) // 2:])

            i, j = 0, 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            res.extend(left[i:])
            res.extend(right[j:])

            return res

        return mergesort(nums)