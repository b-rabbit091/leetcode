class Solution:
    def minimumSum(self, num: int) -> int:
        li = []
        while num > 0:
            ele = num % 10
            li.append(ele)
            num = num // 10
        li = sorted(li)
        num1, num2 = '', ''
        for i in range(len(li)):
            if i % 2 == 0:
                num1 += str(li[i])
            else:
                num2 += str(li[i])
        return int(num1) + int(num2)


num = 2932
sol = Solution()
print(sol.minimumSum(num))
