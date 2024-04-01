medals = ["Gold", "Silver", "Bronze"]


def grade(rank):
    if rank < 3:
        return f"{medals[rank]} Medal"
    return str(rank + 1)


class Solution:
    def findRelativeRanks(self, scores: list[int]) -> list[str]:
        ranks = {score: i for i, score in enumerate(sorted(scores))}
        return [grade(ranks[score]) for score in scores]
