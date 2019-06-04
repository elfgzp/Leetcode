class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        因为Python的整数不是固定的32位，所以需要做一些特殊的处理，具体见代码吧。 
        代码里的将一个数对0x100000000取模（注意：Python的取模运算结果恒为非负数），
        是希望该数的二进制表示从第32位开始到更高的位都同是0（最低位是第0位），以在0-31位上模拟一个32位的int。
        """
        if b == 0:
            return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)
        
        a, b = (a ^ b) % 0x100000000 , ((a & b) << 1) % 0x100000000
        return self.getSum(a, b)

