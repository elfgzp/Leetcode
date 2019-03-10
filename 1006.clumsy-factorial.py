class Solution:
    ops = ['*', '/', '+', '-']
    
    def clumsy(self, N: int) -> int:
        answer = [N]
        
        i = N - 1
        
        j = 0
        while i > 0:
            op = self.ops[j % 4]
            j += 1
            
            if op == '*':
                n = answer.pop(-1)
                val = n * i
                answer.append(val)
                i -= 1
                continue
                
            if op == '/':
                n = answer.pop(-1)
                val = int(n / i)
                answer.append(val)
                i -= 1
                continue
                
            if op == '+':
                answer.append(i)
                i -= 1
                continue
                
            if op == '-':
                answer.append(-i)
                i -= 1
                continue
            
        

        answer = sum(answer)
        
        if answer < -2 ** 31:
            return -2 ** 31
        
        if answer > 2 ** 31 - 1:
            return 2 ** 31 - 1
        
        return answer
        
        