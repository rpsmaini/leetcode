class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum=0
        prod=1
        num=0
        while n>0:
            num=n%10
            Sum = Sum + num
            prod = prod * num
            n = n//10
        return prod-Sum
