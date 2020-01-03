import heapq

'''
Runtime: 84 ms, faster than 99.67% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 16.6 MB, less than 69.57% of Python3 online submissions for Kth Largest Element in a Stream.
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_heap = nums
        # change list to heap
        heapq.heapify(self.k_heap)
        while len(self.k_heap) > k:
            heapq.heappop(self.k_heap)
        
    def add(self, val: int) -> int:
        if len(self.k_heap) < self.k:
            heapq.heappush(self.k_heap, val)
        else:
            heapq.heappushpop(self.k_heap, val)
        return self.k_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
