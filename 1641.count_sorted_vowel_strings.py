from functools import cache


@cache
def strings(letters, length):
    if length == 1:
        return letters
    if letters == 1:
        return 1
    return sum(strings(subletters, length - 1) for subletters in range(1, letters))


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return strings(5,n)
