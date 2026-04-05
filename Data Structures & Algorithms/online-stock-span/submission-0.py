class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        i = len(self.stack) - 1
        while i >= 0 and price >= self.stack[i]:
            i -= 1
        return len(self.stack) - i - 1 if i >= 0 else len(self.stack)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)