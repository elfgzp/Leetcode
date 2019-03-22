#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (47.45%)
# Total Accepted:    19.4K
# Total Submissions: 40.3K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 
# 
# 示例:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
#

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = None
        self._stack = []
        

    def push(self, x: int) -> None:
        if self._min is None:
            self._min = x
        else:
            self._min = min(self._min, x)
        
        self._stack.append(x)
        

    def pop(self) -> None:
        self._stack.pop(-1)
        if self._stack:
            self._min = min(self._stack)
        else:
            self._min = None

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
