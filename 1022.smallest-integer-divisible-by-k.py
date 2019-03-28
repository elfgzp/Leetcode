class Solution:
    def smallestRepunitDivByK1(self, K: int) -> int:
        """
        没搞懂，数学知识 https://blog.csdn.net/qq_17550379/article/details/88780613
        """
        if K % 2 == 0 or K % 5 == 0: 
            return -1
        
        r = 0
        for N in range(1, K + 1):
            r = (r * 10 + 1) % K
            if r == 0: 
                return N
