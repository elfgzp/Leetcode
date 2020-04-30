func squareSum(num int) int {
    sum := 0
    for num != 0 {
        remainder := num % 10
        sum = sum + remainder * remainder
        num = num / 10
    }
    return sum
}


func isHappy(n int) bool {
    slow := squareSum(n)
    fast := squareSum(n)
    fast = squareSum(fast)
    for fast != slow {
        slow = squareSum(slow)
        fast = squareSum(fast)
        fast = squareSum(fast)
    }
    return slow == 1
}
