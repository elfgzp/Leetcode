class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        _min, _max, avg, mid, most = None, 0, 0, 0, 0
        most_count = 0
        total_num_count = 0
        num_indices = []
        offset = 0
        
        _sum = 0
        for num, c in enumerate(count):
            if c != 0:
                if _min is None:
                    _min = num
                
                _max = num
                _sum = (num * c) + _sum
                num_indices.append((offset, c, num))
                offset += c
                total_num_count += c
                
                if c > most_count:
                    most_count = c
                    most = num
                        
        avg = _sum / float(total_num_count)
        
        
        mid_pos = total_num_count // 2
        j = 0
        print(num_indices)
        print(total_num_count)
        for index, t in enumerate(num_indices):
            i, c, num = t
            if i + c >= mid_pos:
                if total_num_count % 2 == 0:
                    if i == mid_pos:
                        _, _, ln = num_indices[index - 1]
                        mid = (ln + num) / float(2)
                    elif i + c == mid_pos:
                        _, _, ln = num_indices[index + 1]
                        mid = (ln + num) / float(2)
                    else:
                        mid = float(num)
                else:
                    mid = float(num)
                break
            
        _min = 0 if _min is None else _min
        return [float(_min), float(_max), avg, mid, float(most)]

