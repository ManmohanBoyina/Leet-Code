class MovingAverage:

    def __init__(self, size: int):
        self.size=size
        self.queue=collections.deque()
        self.sum=0

    def next(self, val: int) -> float:
        avg=0
        self.queue.append(val)
        while len(self.queue)>self.size:
            self.sum-=self.queue.popleft()
        self.sum+=val
        if len(self.queue)>0:
            avg=self.sum/(len(self.queue))
        return avg
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)