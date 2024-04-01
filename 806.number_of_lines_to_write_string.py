LOWERCASE = "abcdefghijklmnopqrstuvwxyz"


class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        c_width = {c: w for w, c in zip(widths, LOWERCASE)}
        cursor = 0
        lines = 1
        for c in s:
            w = c_width[c]
            if cursor + w <= 100:
                cursor += w
            else:
                cursor = w
                lines += 1
        return [lines, cursor]
