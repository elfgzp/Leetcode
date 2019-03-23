#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode-cn.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (57.69%)
# Total Accepted:    11.1K
# Total Submissions: 19K
# Testcase Example:  '1'
#
# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 
# 1. 如果 n 是3的倍数，输出“Fizz”；
# 
# 2. 如果 n 是5的倍数，输出“Buzz”；
# 
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
# 
# 示例：
# 
# n = 15,
# 
# 返回:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            self._fizzBuzz(i)
            for i in range(1, n + 1)
        ]
    
    def _fizzBuzz(self, n: int) -> str:
        fizz = n % 3 == 0
        buzz = n % 5 == 0
        
        s = ''
        
        if fizz:
            s += 'Fizz'
        
        if buzz:
            s += 'Buzz'
        
        return s if s else str(n)
        

