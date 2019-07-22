class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        word_hash = {word for word in wordDict}
        
        dp = [False for _ in range(length)]
        
        dp[0] = s[0] in word_hash
        
        for i in range(1, length):
            if s[:i + 1] in word_hash:
                dp[i] = True
                continue
            
            for j in range(i):
                if dp[j] and s[j + 1: i + 1] in word_hash:
                    dp[i] = True
                    break
        
        return dp[-1]

