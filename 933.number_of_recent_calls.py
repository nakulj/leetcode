from collections import defaultdict

def count_below(vals, cutoff):
    if len(vals) == 0 or vals[-1] < cutoff
        return 0
    if vals[0] >= cutoff:
        return len(vals)
    m = len(vals) // 2
    return count_below(vals[:m],cutoff) + count_below(vals[m:],cutoff)

class RecentCounter:
    def __init__(self):
        self.pings = defaultdict(list)

    def ping(self, t: int) -> int:
        k = t // 3000
        self.pings[k].append(t)

        return len(self.pings[k]) + count_below(self.pings[k-1],t-3000)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
