class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = 0
        pre_sum = 0
        dic = {0: 1}

        for n in nums:
            pre_sum += n
            if pre_sum - k in dic:
                res += dic[pre_sum - k]

            dic[pre_sum] = dic.get(pre_sum, 0) + 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))
