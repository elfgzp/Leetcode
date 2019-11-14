class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)

        while i < length:
            if nums[i] == val:
                nums[i:] = nums[i + 1:]
                length -= 1
            else:
                i += 1

        return length
