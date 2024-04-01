class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        odds = (num for num in nums if num % 2 == 1)
        evens = (num for num in nums if num % 2 == 0)

        def get():
            while (e := next(evens, None)) is not None:
                yield e
                yield next(odds)

        return list(get())
