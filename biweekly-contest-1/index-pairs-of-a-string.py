class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        ans = []
        for word in words:
            length = len(word)
            i = 0
            while True:
                i = text.find(word, i)
                if i == -1:
                    break

                ans.append([i, i + length - 1])
                i += 1

        ans.sort(key=lambda x: (x[0], x[1]))
        return ans

