class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        import re
        return re.findall(r'(?<='+ first + '\s' + second + ')' + '\s(\w+)\s*', text)

