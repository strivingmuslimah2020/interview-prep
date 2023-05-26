class Solution:
    def fib(self, n: int) -> int:
        
        store = defaultdict(int)
        if n == 0 or n == 1:
            return n
        elif n in store:
            return store[n]
        else:
            store[n] = self.fib(n - 1) + self.fib(n - 2)
            return store[n]