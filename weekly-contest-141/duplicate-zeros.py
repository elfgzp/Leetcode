class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        
        i = 0
        while i < length:
            if arr[i] == 0:
                arr[::] = list(arr[:i + 1] + [0] + arr[i + 1:])[:length]
                i += 2
            else:
                i += 1

