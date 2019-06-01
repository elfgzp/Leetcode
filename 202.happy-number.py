class Solution:
    def isHappy(self, n: int) -> bool:
        history = {n}
        while n != 1:
            n = sum(list(map(lambda x : int(x) ** 2, str(n))))
            if n in history:
                return False
            history.add(n)
            
        else:
            return True
            

