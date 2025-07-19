class RecentCounter:

    def __init__(self):
        self.call=deque()

    def ping(self, t: int) -> int:
        self.call.append(t)
        time=t-3000
        while self.call and self.call[0]<time:
            self.call.popleft()
        return len(self.call)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)