'''
Time Limit Exceeded
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = self._quicksort(nums)
        self.k_largest = self.nums[:k]

    def _quicksort(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        if len(nums) <= 1:
            return nums
        
        pivot = nums[0]
        pivot_count = 0
        for num in nums:
            if num < pivot:
                right.append(num)
            elif num > pivot:
                left.append(num)
            else:
                pivot_count += 1
                
        left = self._quicksort(left)
        right = self._quicksort(right)
        return left + [pivot] * pivot_count + right
    
    def _find_index_bug(self, val:int) -> int:
        '''
        Find the right index to insert the val in the k_largest part.
        '''
        inserted_idx = -1
        middle = self.k_largest[min(self.k // 2, max(len(self.nums) - 1, 0))]
        if val < middle:
            for i in range(self.k-1, self.k // 2, -1):
                if self.k_largest[i] > val:
                    inserted_idx = i + 1
                    break
        elif val > middle:
            for i in range(0, self.k // 2 + 1):
                if self.k_largest[i] < val:
                    inserted_idx = i
                    break
        else:
            inserted_idx = self.k // 2

        return inserted_idx

    def _find_index(self, val:int) -> int:
        '''
        Find the right index to insert the val in the k_largest part.
        '''
        inserted_idx = -1
        for i, e in enumerate(self.k_largest):
            if e < val:
                inserted_idx = i
                break
        if inserted_idx == -1:
            inserted_idx = i + 1
        return inserted_idx
                
        
    def add(self, val: int) -> int:         
        if not self.k_largest or val <= self.k_largest[-1]:
            self.nums.append(val)
            self.k_largest = self.nums[:self.k]
            return self.nums[self.k - 1]
        
        # keep k_largest part sorted
        inserted_idx = self._find_index(val)
        # special case that inserted val is the largest, in this case, inserted_idx is -1
        inserted_idx = max(0, inserted_idx)
        self.nums = self.nums[:inserted_idx] + [val] + self.nums[inserted_idx:]
        # update k_largest part
        self.k_largest = self.nums[:self.k]

        return self.nums[self.k - 1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
