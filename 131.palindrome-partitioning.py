class Solution:
    ans = None
    length = None
    s = None
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        
        if not s:
            return self.ans
        
        self.s = s
        self.length = len(s)            
        
        self._partition()
        return self.ans
    
    def _partition(self, start=0, res=None):
        if res is None:
            res = []
        
        if res is None:
            res = []
            
        if start >= self.length:
            self.ans.append(res)
            return

        for end in range(start + 1, self.length + 1):
            sub = self.s[start: end]
            if sub == sub[::-1]:
                self._partition(end, res + [sub])

