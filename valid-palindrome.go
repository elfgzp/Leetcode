import "strings"

func isPalindrome(s string) bool {
    s = strings.ToLower(s)
    l, r := 0, len(s) - 1
    for l < r {
        for l < r && !isalnum(s[l]) {
            l ++
        }
        
        for l < r && !isalnum(s[r]) {
            r --
        }
        
        if l < r {
            if s[l] != s[r] {
                return false
            }
            
            l++
            r--
        }
    }
    return true
}

func isalnum(c byte) bool {
    return (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')
}
