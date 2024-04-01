from typing import Iterator



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while  s[i] == ' ':
            i-=1
        r = i
        while s[i] != ' ':
            if i == 0:
                return r+1
            i-=1
        l = i
        return r-l
        
