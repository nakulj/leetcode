class Solution:
    def reverseWords(self, s: str) -> str:
       words = s.split(' ') 
       return ' '.join(''.join(reversed(word) for word in words)
