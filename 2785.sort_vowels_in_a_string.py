vowels =set(  'aeiouAEIOU' )

class Solution:
    def sortVowels(self, s: str) -> str:
        all_vowels = sorted(( c for c in s if c in vowels ),reverse=True)
        return ''.join(c if c not in vowels else all_vowels.pop(-1) for c in s)
