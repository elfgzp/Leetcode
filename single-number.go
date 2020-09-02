package Leetcode

import "sort"

func singleNumber(nums []int) int {
sort.Ints(nums)

result := 0
for _, n := range nums {
result ^= n
}
return result
}
