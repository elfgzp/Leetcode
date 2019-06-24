import collections
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hashmap = collections.defaultdict(int)
        for n, s, e in trips:
            hashmap[s] += n
            hashmap[e] -= n
            
        cur = 0
        for i in sorted(hashmap):
            cur += hashmap[i]
            if cur > capacity:
                return False
            
        return True
