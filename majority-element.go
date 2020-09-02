package Leetcode

func majorityElement(nums []int) int {
	count := 1
	cur := nums[0]
	for i:= 1; i < len(nums); i ++ {
		if count == 0 {
			cur = nums[i]
		}

		if cur == nums[i] {
			count += 1
		} else {
			count -= 1
		}
	}
	return cur
}
