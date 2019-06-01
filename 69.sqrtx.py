class Solution1:
    """
    二分查找法
    """
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        left, right = 0, x
        while left <= right:
            mid = (left + right) / 2.0
            if int(mid**2) > x:
                right = mid
            elif int(mid**2) < x:
                left = mid
            else:
                return int(mid)
            
    
class Solution:
    """
    牛顿迭代法
    """
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        ans = x / 2.0
        while ans**2 - x >= 1:
            ans = (ans + x / ans) / 2

        return int(ans)
