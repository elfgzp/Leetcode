class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        """
        利用滑动窗口法，假设起始时窗口左端和右端 [i, j] 为 [0, 0]，
        右端开始向右延伸 j += 1，
        当 A[j] 为 1 时不做处理，继续延伸，
        当 A[j] 为 0 时，K 数量减一，K -= 1

        若 K 小于零，则 窗口左端需要向右移动直到超过一个 0 来补充 K 的数量。
        while K < 0:
            if A[left] == 1:
                        left += 1
            else:
                left += 1
                K += 1

        期间不断计算窗口最大值，直到右端到 A 的末尾。
        """
        left, right = 0, 0
        max_len = 0

        while right < len(A):
            if A[right] == 1:
                right += 1
            else:
                right += 1
                K -= 1
                
                while K < 0:
                    if A[left] == 1:
                        left += 1
                    else:
                        left += 1
                        K += 1
                        
            max_len = max(right - left, max_len)
        
        return max_len

        