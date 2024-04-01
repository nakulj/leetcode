import heapq

class Heap:
    def __init__(self, capacity:int, None) -> None:
        self.key = key
        self.capacity = capacity
        self.h = []

    def push(self,value):
        keyed = ( self.key(value),value )
        if len(self.h) < self.capacity:
            heapq.heappush(self.h, keyed)
        else:
            heapq.heappushpop(self.h,keyed)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        h = Heap()
        

    def add(self, val: int) -> int:
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
