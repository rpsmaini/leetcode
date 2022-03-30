#Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort() #solution 
        salary.pop(0)
        salary.pop(-1)
        a=len(salary)
        b=sum(salary)
        res=b/a
        return res
