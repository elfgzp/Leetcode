func longestPalindrome(s string) string {
    length := len(s)
    if length < 0 {
        return ""
    }
    
    dp := make([][]bool, length)
    
    start, maxLen := 0, 1
    for r := 0; r < length; r ++ {
        dp[r] = make([]bool, length)
        dp[r][r] = true
        for l := 0; l < r; l ++ {
            if s[l] == s[r] && (r - l <= 2 || dp[l + 1][r - 1] == true) {
                dp[l][r] = true
            } else {
                dp[l][r] = false
            }
            
            if dp[l][r] && r - l + 1 > maxLen {
                curLen := r - l + 1
                if curLen > maxLen {
                    start = l
                    maxLen = curLen
                }
            }
        }
    }
    return s[start: start + maxLen]
}
