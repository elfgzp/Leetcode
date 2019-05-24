class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: (x[0], x[0] - x[1]))

        res = [intervals[0]]

        for each in intervals[1:]:
            left, right = each
            if res[-1][0] == left:
                continue
            elif res[-1][1] >= left:
                if res[-1][1] < right:
                    res[-1][1] = right
            else:
                res.append(each)
        
        return res


