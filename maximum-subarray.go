func maxSubArray(nums []int) int {
    // if len(nums) < 1 {
    //     return 0
    // }
    pre, max := nums[0], nums[0]
    
    for i := 1;i < len(nums); i ++ {
        if pre + nums[i] > nums[i] {
            pre = pre + nums[i]
        } else {
            pre = nums[i]
        }
        
        if pre > max {
            max = pre
        }
    }
    return max
}
