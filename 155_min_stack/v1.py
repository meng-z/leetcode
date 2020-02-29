class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # append a tuple in format of (val, current minimum)
        self.vals = list()
        

    def push(self, x: int) -> None:
        # when it is empty, current mininum equals to val
        if not self.vals:
            self.vals.append((x, x))
            return
            
        curr_min = self.getMin()
        if x < curr_min:
            curr_min = x
            
        self.vals.append((x, curr_min))
        

    def pop(self) -> None:
        self.vals.pop()
        

    def top(self) -> int:
        return self.vals[-1][0]
        

    def getMin(self) -> int:
        return self.vals[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
