class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for idx in range(len(digits) - 1, -1, -1):
            if carry:
                if digits[idx] == 9:
                    digits[idx] = -1
                else:
                    carry = 0
                digits[idx] += 1

            if carry == 0:
                return digits
            print(digits)
        return [1] + digits

