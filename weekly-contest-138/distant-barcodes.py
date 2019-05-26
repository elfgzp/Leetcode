class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        
        counter = Counter(barcodes)
        els = [e[0] for e in counter.most_common()]
        
        ans = []
        while els:
            if len(els) < 2:
                ans.append(els[0])
                els.pop(0)
                break
            
            if not ans or ans[-1] != els[0]:
                ans.append(els[0])
                counter[els[0]] -= 1
                
                if counter[els[0]] == 0:
                    els.pop(0)
                elif counter[els[0]] < counter[els[1]]:
                    els[0], els[1] = els[1], els[0]
                    
            else:
                ans.append(els[1])
                counter[els[1]] -= 1
                
                if counter[els[1]] == 0:
                    els.pop(1)
                elif len(els) >= 3 and counter[els[1]] < counter[els[2]]:
                    els[1], els[2] = els[2], els[1]
        
        return ans

