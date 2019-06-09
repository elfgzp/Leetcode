class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        from copy import copy
        counter = dict(Counter(tiles))
        ans = []
        def _helper(co, s):
            if not co:
                return 
            
            for c in co.keys():
                _co = copy(co)
                _co[c] -= 1
                ans.append(s + c)
                if _co[c] == 0:
                    _co.pop(c)
                _helper(_co, s + c)
        
        _helper(counter, '')
        return len(ans)
                
