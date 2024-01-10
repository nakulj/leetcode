from typing import Iterator


def zigzag(n) -> Iterator[int]:
    while True:
        yield from range(n)
        yield from range(n - 2, 0, -1)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows:list[list[str]] = [[] for _ in range(numRows)]
        for c, row in zip(s, zigzag(numRows)):
            rows[row].append(c)
        return "".join("".join(row) for row in rows)
