class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        ans = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                digit += ans[i + j]
                ans[i + j] = digit % 10
                # print(digit, ans)
                ans[i + j + 1] += digit // 10
                # print(ans)
            # print()

        ans = ans[::-1]
        while ans[0] == 0:
            ans = ans[1:]

        s = ""
        for x in ans:
            s += str(x)
        return s