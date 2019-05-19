class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        
        for s in S:
            if stack and stack[-1] == s:
                stack.pop(-1)
            else:
                stack.append(s)
        
        if stack:
            return ''.join(stack)
        
        return ''
