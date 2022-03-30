#Count Odd Numbers in an Interval Range
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if(low%2==0):
            low=low+1
        if(high%2==0):
            high=high-1
        count = (high-low)//2
        return count+1
